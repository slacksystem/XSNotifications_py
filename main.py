from XSONotifications import XSOMessage, XSNotifier

msg = XSOMessage()
msg.messageType = 1
msg.title = "Example Notification!"
msg.content = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
msg.sourceApp = "XSNoti Python Test!"
msg.opacity = 0.7

XSNotifier = XSNotifier()

XSNotifier.send_notification(msg)