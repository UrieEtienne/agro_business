def is_admin(user):

    return user.role == 'admin'


def is_commercial(user):

    return user.role == 'commercial'


def is_communication(user):

    return user.role == 'communication'


def is_comptable(user):

    return user.role == 'comptable'