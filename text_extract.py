import symbl
import transcript
import os

global run_full_magic

run_full_magic = False

def text_extract_func():
    parameters_object={'sentiment': True}

    the_path = os.getenv('the_path', r'C:\Users\Adit\Pictures\Camera Roll\\try.mp4')
    # C:\Users\Adit\Pictures\Camera Roll\try.mp4
    word = os.getenv('data', 'query')

    _, conv_id = transcript.perform_magic()
    most_recent = (word, the_path)
    conversation = symbl.Conversations.get_messages(conversation_id=conv_id, parameters = parameters_object)

    prev_conv_id = conv_id
    messages = []
    for message in conversation.messages:
        messages.append(message.text)

    final_text = ("")

    for i in messages :
        final_text = (final_text + " " + str(i))

    return final_text



