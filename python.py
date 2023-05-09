import telegram.ext

with open('token.txt', 'r') as f:
    TOKEN = f.read()


def start(update, context):
    update.message.reply_text("Hello! Welcome to my new Bot! "
                              "I am exited to tell you about my projects. "
                              "Please use the following commands to readily navigate. "
                              "\nThe Following Commands Are Available: "
                              "\n/start -> Welcome Message "
                              "\n/help -> The Available Commands "
                              "\n/content -> Information About This Project "
                              "\n/contact -> My Contact "
                              "\n/aboutme -> About Me Section")


def help(update, context):
    update.message.reply_text("The Following Commands Are Available:"
                              "\n/start -> Welcome Message"
                              "\n/help -> This Message"
                              "\n/content -> Information About This Project"
                              "\n/contact -> My Contact"
                              "\n/aboutme -> About Me Section")


def content(update, context):
    update.message.reply_text("Introducing AboutMeBot, the personal bot "
                              "that tells you all about me! With this bot, "
                              "you can get to know me better, learn about my skills, "
                              "experience, and interests, and discover what sets me apart "
                              "from others in my field. Whether you're a potential employer, "
                              "colleague, or just curious about who I am, this bot is the perfect "
                              "way to get a quick and comprehensive overview of my professional profile. "
                              "So what are you waiting for? Say /start to AboutMeBot today and let's get acquainted!")


def aboutMe(update, context):
    update.message.reply_text("Hi there, I'm Gor Hayrapetyuan! "
                              "I'm pursuing a degree in Computer Science at "
                              "the American University of Armenia. I have a "
                              "strong foundation in programming, having passed "
                              "various courses and gained experience with "
                              "languages such as C, C++, Python, Java, and JavaScript. "
                              "I'm excited to share more about my skills and interests "
                              "with you, so feel free to take a look at my GitHub and Linkedin profiles: "
                              "\ncommand -> /contact! ")


def contact(update, context):
    update.message.reply_text("Gor V. Hayrapetyan"
                              "\nYerevan, Armenia"
                              "\nEmail - ghayrapetyan890@gmail.com"
                              "\nPhone Number - +374 44 416-440"
                              "\nLinkedIn - linkedin.com/in/gorhayrapetyann/"
                              "\nGitHub - github.com/gorhayrapetian"
                              "\nTwitter - twitter.com/gorhayrapetyann")


updater = telegram.ext.Updater(TOKEN, use_context=True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler("start", start))
disp.add_handler(telegram.ext.CommandHandler("help", help))
disp.add_handler(telegram.ext.CommandHandler("content", content))
disp.add_handler(telegram.ext.CommandHandler("contact", contact))
disp.add_handler(telegram.ext.CommandHandler("aboutme", aboutMe))

updater.start_polling()
updater.idle()
