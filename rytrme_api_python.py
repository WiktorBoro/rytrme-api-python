from requests import get, post
from re import match


def get_id(our_parametr: str,
           api_headers: dict,
           url: str,
           use_case_detal: set[str]):

    response_id = get(url, headers=api_headers)

    for data in response_id.json()['data']:
        # if we input name instead id, function get id based on name
        if data["name"] != our_parametr:
            continue
        # if we change use-cases, function check we add correct 'contextInputs'
        if url == 'https://api.rytr.me/v1/use-cases':
            if set(use_case_detal) != set(keyLabel['keyLabel'] for keyLabel in data['contextInputs']):
                raise Exception(f"Invalid parameter: {use_case_detal}")
        return data["_id"]
    raise Exception(f"Invalid parameter: {our_parametr}")


def get_text_from_rytr_me_api(api_key: str,
                              input_contexts: dict[str:str],
                              language='607adac76f8fe5000c1e636d',
                              tone='60572a639bdd4272b8fe358a',
                              use_case='60584cf2c2cdaa000c2a7954',
                              variations=1,
                              user_id='USER1',
                              formats='html',
                              creativity_level='default'):

    api_headers = {"Authentication": f"Bearer {api_key}",
                   "Content-Type": "application/json"}

    # pattern checks user entered id, if not we looking id by name
    token_pattern = r'^[0-9a-z]{20,26}$'

    id_dict = {
                'language_id': language if match(token_pattern, language)
                else get_id(our_parametr=language,
                            api_headers=api_headers,
                            url='https://api.rytr.me/v1/languages',
                            use_case_detal=set()),

                'tone_id': tone if match(token_pattern, tone)
                else get_id(our_parametr=tone,
                            api_headers=api_headers,
                            url='https://api.rytr.me/v1/tones',
                            use_case_detal=set()),

                'use_case_id': use_case if match(token_pattern, use_case)
                else get_id(our_parametr=use_case,
                            api_headers=api_headers,
                            url='https://api.rytr.me/v1/use-cases',
                            use_case_detal=set(input_contexts_key for input_contexts_key in input_contexts))
               }

    data = {
        'languageId': id_dict['language_id'],
        'toneId': id_dict['tone_id'],
        'useCaseId': id_dict['use_case_id'],
        'inputContexts': input_contexts,
        'variations': variations,
        'userId': user_id,
        'format': formats,
        'creativityLevel': creativity_level,
    }

    api_response = post('https://api.rytr.me/v1/ryte', headers=api_headers, json=data)
    if api_response.json()['success']:
        return api_response.json()['data']
    else:
        return api_response.json()
