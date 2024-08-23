import requests
from bs4 import BeautifulSoup
from datetime import datetime

def convert_reputation(reputation_str):
    # Remove commas from the string
    reputation_str = reputation_str.replace(',', '')
    
    if 'k' in reputation_str:
        return int(float(reputation_str.replace('k', '')) * 1000)
    elif 'm' in reputation_str:
        return int(float(reputation_str.replace('m', '')) * 1000000)
    else:
        return int(reputation_str)

def convert_date(time_str):
    # Convert StackOverflow date format to Unix timestamp
    date_obj = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
    return int(date_obj.timestamp())

def safe_get_text(element, default='0'):
    return element.get_text() if element else default

def get_questions(tag=None):
    url = "https://stackoverflow.com/questions"
    if tag:
        url += f"?tagged={tag}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    questions = []
    for question in soup.select('.s-post-summary'):
        # Extract tags
        tags = [tag.get_text() for tag in question.select('.js-post-tag-list-wrapper .post-tag')]
        
        # Extract owner details
        owner_section = question.select_one('.s-user-card')
        profile_link = owner_section.select_one('.s-user-card--link a')['href'] if owner_section and owner_section.select_one('.s-user-card--link a') else None
        user_id = profile_link.split('/')[2] if profile_link else 'N/A'
        
        reputation_str = safe_get_text(owner_section.select_one('.s-user-card--rep'), '0')
        reputation = convert_reputation(reputation_str)
        
        owner = {
            'account_id': 'N/A',  # Need to find an example where this is present
            'reputation': reputation,
            'user_id': int(user_id),
            'user_type': 'registered' if owner_section else 'unregistered',
            'profile_image': owner_section.select_one('img')['src'] if owner_section and owner_section.select_one('img') else '',
            'display_name': safe_get_text(owner_section.select_one('.s-user-card--link a')),
            'link': "https://stackoverflow.com" + profile_link if profile_link else ''
        }
        
        # Extract metadata
        question_id = int(question['data-post-id'])
        score = int(safe_get_text(question.select_one('.s-post-summary--stats-item-number')))
        view_count = int(safe_get_text(question.select_one('[title$="views"] .s-post-summary--stats-item-number'), '0'))
        
        # This might or might not be correct, double triple check
        answer_count = int(safe_get_text(question.select_one('.s-post-summary--stats-item[title$="answers"] .s-post-summary--stats-item-number')))
        
        # Extract dates
        time_element = question.select_one('.s-user-card--time span')
        creation_date_str = time_element['title'] if time_element else ''
        creation_date = convert_date(creation_date_str.replace('Z', '').replace('T', ' '))
        
        last_activity_date = creation_date  # Will Change this later
        
        # Check if the question has an accepted answer
        has_accepted_answer = "has-accepted-answer" in question.select_one('.has-answers')['class'] if question.select_one('.has-answers') else False
        accepted_answer_id = question_id if has_accepted_answer else None
        
        # Add to the list
        questions.append({
            'tags': tags,
            'owner': owner,
            'is_answered': answer_count > 0,
            'view_count': view_count,
            'accepted_answer_id': accepted_answer_id,
            'answer_count': answer_count,
            'score': score,
            'last_activity_date': last_activity_date,
            'creation_date': creation_date,
            'last_edit_date': last_activity_date,
            'question_id': question_id,
            'link': "https://stackoverflow.com" + question.select_one('.s-post-summary--content-title a')['href'],
            'closed_date': None,  # Couldn't find an example where the question was closed so find one and implement it
            'closed_reason': None,  
            'title': safe_get_text(question.select_one('.s-post-summary--content-title a'))
        })
    
    return questions