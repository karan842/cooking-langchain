css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://th.bing.com/th/id/OIP.0OUoxz6bqF45R-5CZwqVagHaHZ?pid=ImgDet&rs=1" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://th.bing.com/th/id/R.b544146a8e95908f097fe86343f9140b?rik=jX7vw4SGwprkmQ&riu=http%3a%2f%2fgetdrawings.com%2ffree-icon%2fhuman-icon-png-68.png&ehk=6%2fQzY0BOQSjQjQezTPTHGr%2fZ7zGlyHnCLtaD9hyBwKs%3d&risl=&pid=ImgRaw&r=0">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''