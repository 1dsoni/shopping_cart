from djchoices import DjangoChoices, ChoiceItem


class UserRoleChoice(DjangoChoices):
    admin = ChoiceItem("admin")
    user = ChoiceItem("user")


class UserStatusChoice(DjangoChoices):
    active = ChoiceItem("active")
    blocked = ChoiceItem("blocked")
