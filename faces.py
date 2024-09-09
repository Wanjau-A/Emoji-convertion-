def main():
    variable_faces = input("Enter your message: ")
    print(f"Send: {change_faces(variable_faces)}")


def change_faces(message):
    message = message.replace(":)", "🙂")
    message = message.replace(":(", "🙁")
    return message

main() 