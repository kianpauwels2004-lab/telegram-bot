from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

from telegram.ext import (
    ApplicationBuilder,
    ChatJoinRequestHandler,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
)

TOKEN = "8586831591:AAGjCLUWrdqwlfN1ADBNNwQg7GBAOWpeie0"

SUPPORT_USERNAME = "PWLSKIAN"


async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    await update.message.reply_text(
        "Bot is live ✅"
    )


async def join_request(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    user = update.chat_join_request.from_user

    keyboard = [
        [
            InlineKeyboardButton(
                "I'm 18+ ✅",
                callback_data="age_ok",
            )
        ]
    ]

    await context.bot.send_message(
        chat_id=user.id,
        text=(
            "Welcome to My Laboratory 🚀\n\n"
            "You've been accepted into our free public channel.\n\n"
            "• Free market analysis 📈\n"
            "• Free webinars 🎓\n"
            "• Member results 🔥\n\n"
            "Continue only if you're 18+ 🔞"
        ),
        reply_markup=InlineKeyboardMarkup(
            keyboard
        ),
    )


async def button_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    query = update.callback_query

    await query.answer()

    if query.data == "age_ok":

        keyboard = [
            [
                InlineKeyboardButton(
                    "Contact Support 💬",
                    url=(
                        "https://t.me/"
                        + SUPPORT_USERNAME
                    ),
                )
            ]
        ]

        await query.edit_message_text(
            text=(
                "Perfect! 👈\n\n"
                "I'll let you contact "
                "the support team directly 👇"
            ),
            reply_markup=InlineKeyboardMarkup(
                keyboard
            ),
        )


app = (
    ApplicationBuilder()
    .token(TOKEN)
    .build()
)

app.add_handler(
    CommandHandler(
        "start",
        start,
    )
)

app.add_handler(
    ChatJoinRequestHandler(
        join_request
    )
)

app.add_handler(
    CallbackQueryHandler(
        button_handler
    )
)

print("Bot running...")

app.run_polling()