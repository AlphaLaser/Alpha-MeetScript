import symbl
import os







the_path = os.getenv('the_path', r'C:\Users\Adit\Pictures\Camera Roll\\try.mp4')
#C:\Users\Adit\Pictures\Camera Roll\try.mp4
word = os.getenv('data', 'query')


#word = input("Search for word : ")
print("Loading...")

local_path = (r"{}").format(the_path)

conversation_object = symbl.Video.process_file(
file_path=local_path)

# Generate transcript
# print(conversation_object.get_messages())

conv_id = (conversation_object.get_conversation_id())

def perform_magic():
    the_path = os.getenv('the_path', r'C:\Users\Adit\Pictures\Camera Roll\\try.mp4')
    # C:\Users\Adit\Pictures\Camera Roll\try.mp4
    word = os.getenv('data', 'query')


    if the_path == os.getenv('prev_the_path', 'zzz') and word == os.getenv('prev_data', 'zzz'):
        return word, os.environ['prev_conv_id']
    print("Loading...")

    local_path = (r"{}").format(the_path)

    conversation_object = symbl.Video.process_file(
        file_path=local_path)

    # Generate transcript
    # print(conversation_object.get_messages())

    conv_id = (conversation_object.get_conversation_id())
    os.environ['prev_data'] = word
    os.environ['prev_the_path'] = the_path
    os.environ['prev_conv_id'] = conv_id
    return word, conv_id