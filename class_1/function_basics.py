
def send_email_to_user(user):
    if is_active(user):
        send_email(user.email)
        return True

    return False


def send_email_to_user(user):
    if not is_active(user):
        return False

    send_email(user.email)
    return True


# user > Boolean   (is active)
# user > Boolean   (is NOT active)