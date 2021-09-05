from .. import loader, utils

@loader.tds
class AutoReaderMod(loader.Module):
    """Модуль AutoReader"""
    strings = {'name': 'AutoReader'}

    async def client_ready(self, client, db):
        self.db = db

    async def rchatcmd(self, message):
        """
        Используй: .rchat чтобы добавить чат в список!
        или аргумент «all» | включить для всех чатов.
        или аргумент «off» | выключить полностью.
        """
        reader = self.db.get("AutoReader", "reader", [])
        args = utils.get_args_raw(message)
        chat = await message.client.get_entity(message.chat_id)
        if args:
            if args == "all":
                await message.edit("Включено для всех чатов.")
                self.db.set("AutoReader", "reader", True)
                return
            elif args == "off":
                await message.edit("Выключено для всех чатов.")
                self.db.set("AutoReader", "reader", [])
                return
        else:
            try:
                if str(chat.id) not in reader:
                    reader.append(str(chat.id))
                    self.db.set("AutoReader", "reader", reader)
                    await message.edit(f"Чат {chat.title} добавлен в AutoRead список.")
                else:
                    reader.remove(str(chat.id))
                    self.db.set("AutoReader", "reader", reader)
                    await message.edit(f"Чат {chat.title} удален из AutoRead списка.")
            except TypeError: return await message.edit("Режим включен для всех чатов, ты не можешь добавить ещё чат.")

    async def rchatscmd(self, message):
        """Используй: .rchats чтобы посмотреть список AutoRead чатов"""
        await message.edit("ща покажу")
        reader = self.db.get("AutoReader", "reader", [])
        chats = ""
        try:
            for x in reader:
                chat = await message.client.get_entity(int(x))
                chats += f"• {chat.title} | {chat.id}\n"
            await message.edit(f"Всего {len(reader)} AutoRead чатов.\n\n{chats}")
        except TypeError: return await message.edit("Режим включен для всех чатов!")

    async def watcher(self, message):
        """пасхалка: кто прочитал тот должен сотку мне на киви!1!!"""
        try:
            reader = self.db.get("AutoReader", "reader", [])
            for x in reader:
                chat = await message.client.get_entity(int(x))
                if message.mentioned:
                    await message.client.send_read_acknowledge(chat.id, clear_mentions=True)
            if reader is True:
                if message.mentioned:
                    await message.client.send_read_acknowledge(message.chat_id, clear_mentions=True)
        except: pass