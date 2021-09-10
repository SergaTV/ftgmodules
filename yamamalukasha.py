async def boldcmd(self, message):
        """Сделать текст жирным.\nИспользуй: .bold <текст или реплай>."""
        text = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        if text:
            await message.edit(f"<b>{text}</b>")
        if reply:
            if message.from_id != reply.from_id:
                await message.edit(f"<b>{reply.raw_text}</b>")
            else:
                await message.delete()
                await reply.edit(f"<b>{reply.raw_text}</b>")


    async def italiccmd(self, message):
        """Сделать текст курсивным.\nИспользуй: .italic <текст или реплай>."""
        text = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        if text:
            await message.edit(f"<i>{text}</i>")
        if reply:
            if message.from_id != reply.from_id:
                await message.edit(f"<i>{reply.raw_text}</i>")
            else:
                await message.delete()
                await reply.edit(f"<i>{reply.raw_text}</i>")


    async def underlinecmd(self, message):
        """Сделать текст подчеркнутым.\nИспользуй: .underline <текст или реплай>."""
        text = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        if text:
            await message.edit(f"<u>{text}</u>")
        if reply:
            if message.from_id != reply.from_id:
                await message.edit(f"<u>{reply.raw_text}</u>")
            else:
                await message.delete()
                await reply.edit(f"<u>{reply.raw_text}</u>")


    async def monocmd(self, message):
        """Сделать текст моноширинным.\nИспользуй: .mono <текст или реплай>."""
        text = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        if text:
            await message.edit(f"<code>{text}</code>")
        if reply:
            if message.from_id != reply.from_id:
                await message.edit(f"<code>{reply.raw_text}</code>")
            else:
                await message.delete()
                await reply.edit(f"<code>{reply.raw_text}</code>")


    async def crosscmd(self, message):
        """Сделать текст зачеркнутым.\nИспользуй: .cross <текст или реплай>."""
        text = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        if text:
            await message.edit(f"<s>{text}</s>")
        if reply:
            if message.from_id != reply.from_id:
                await message.edit(f"<s>{reply.raw_text}</s>")
            else:
                await message.delete()
                await reply.edit(f"<s>{reply.raw_text}</s>")


    async def entercmd(self, message):
        """Перенос строки после каждого слова.\nИспользуй: .enter <текст или реплай>."""
        text = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        if text:
            await message.respond("\n".join(text.split(' ')))
        if reply:
            await message.edit("\n".join(reply.text.split(' ')))
        await message.delete()