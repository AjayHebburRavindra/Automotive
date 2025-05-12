from win10toast import ToastNotifier

n = ToastNotifier()

n.show_toast(
    'python project',
    'Here is your notification body',
    duration = 20,
    icon_path = 'logo.ico',
)