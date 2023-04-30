class PostOffice:
    """A Post Office class. Allows users to message each other.

    :ivar int message_id: Incremental id of the last message sent.
    :ivar dict boxes: Users' inboxes.

    :param list usernames: Users for which we should create PO Boxes.
    """

    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, message_body, urgent=False, subject = None):
        """Send a message to a recipient.

        :param str sender: The message sender's username.
        :param str recipient: The message recipient's username.
        :param str message_body: The body of the message.
        :param urgent: The urgency of the message.
        :type urgent: bool, optional
        :return: The message ID, auto incremented number.
        :rtype: int
        :raises KeyError: if the recipient does not exist.
        """
        user_box = self.boxes[recipient]
        self.message_id = self.message_id + 1
        message_details = {
            'id': self.message_id,
            'subject': subject,
            'body': message_body,
            'sender': sender,
            'read': False,
        }
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id

    def read_inbox(self, username, text=None):
        """read txt in all inbox of username.

                      :param str username: the name of user name
                      :param str txt: The text to search in message_body or in subject
                      :return: The list of all messages
                      :rtype: list
                      :raises KeyError: if the username does not exist.
                      """

        if text == None:
            text = len(self.boxes[username])
        result = []
        for index in range(0, text):
            message = self.boxes[username][index]
            if not message['read']:
                self.boxes[username]['read'] = True
                result.append(message)

        return result



    def search_inbox(self, username, text):
        """search txt in all inbox of username.

              :param str username: the name of user name
              :param str text: The text to search in message_body or in subject
              :return: The list of all messages
              :rtype: list
              :raises KeyError: if the username does not exist.
              """
        result = [message for message in self.boxes[username] if text in message['body'] or text in message['subject']]

        return result