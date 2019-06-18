import discord
from discord.ext import (
    commands,
)
from discord_interactive import (
    Page,
    Help,
)


class HelpCog(
    commands.Cog
):
    def __init__(
        self,
        client,
    ):
        self.client = client

    @commands.group(
        invoke_without_command=True
    )
    async def help(
        self,
        ctx,
    ):
        root = Page(
            "Welcome to YashBot3001!\nPing Y45HK4R4ND1K4R#9565 on the support server if you have any issues. Use ;help <category> to get all the commands in a single category explained in more detail. Use the reactions to navigate through the menus!"
        )
        page1 = Page(
            "**YashBot3001 Help**\nFun:\n`;8ball [question]`\n`;bully <target>`\n`;kill <target>`\n`;cat`\n`;dice`\n`;dog`\n`;fight <challenger1> <challenger2>`\n`;hamster`\n`;ping`\n`;rps [choice]`\n`;song`\n`;thanos <target>`\n`;coin`\n`;hack <target>`\n`;rate <member>`\n**Anything in [] is required. Anything in <> is optional.**"
        )
        page2 = Page(
            "**YashBot3001 Help**\nMath:\n`;add [number1] [number2]`\n`;cos [number]`\n`;divide [number1] [number2]`\n`;exp [number1] [number2]`\n`;factorial [number]`\n`;multiply [number1] [number2]`\n`;root [number]`\n`;sine [number]`\n`;square [number]`\n`;subtract [number1] [number2]`\n`;tan [number]`\n**Anything in [] is required. Anything in <> is optional.**"
        )
        page3 = Page(
            "**YashBot3001 Help**\nInfo:\n`;help`\n`;info`\n`;invite`\n`;uptime`\n`;source`\n`;guilds`\n`;users`\n**Anything in [] is required. Anything in <> is optional.**"
        )
        page4 = Page(
            "**YashBot3001 Help**\nText Manipulation:\n`;secret <message>`\n`;echo <message>`\n`;embed <message>`\n`;upper [message]`\n`;lower [message]`\n`;reverse [message]`\n`;tts [message]` <------ Works best on computer\n`;ascii [message]` <------ Works best with short messages\n**Anything in [] is required. Anything in <> is optional.**"
        )
        page5 = Page(
            "**YashBot3001 Help**\nImage Manipulation:\n`;kirby [message]`\n`;lisa [message]`\n`;pewds [message]`\n`;gru [message]`\n`;linus [message]`\n`;trump [message]`\n`;elon [message]`\n`;supreme [text]`\n`;deepfry <member>`\n`;sad <member>`\n`;emboss <member>`\n`;invert <member>`\n**Anything in [] is required. Anything in <> is optional.**"
        )
        page6 = Page(
            "**YashBot3001 Help**\nSupport Server Only Commands:\n*These commands only work in the support server. Join it here: https://discord.gg/hG6RDZz*\n`;subscribe`\n`;polls`\n`;unsubscribe`\n**Anything in [] is required. Anything in <> is optional.**"
        )
        page7 = Page(
            "**YashBot3001 Help**\nWeb:\n`;google [query]`\n`;youtube [query]`\n`;wiki [query]`\n**Anything in [] is required. Anything in <> is optional.**"
        )
        page8 = Page(
            "**YashBot3001 Help**\nTags:\n`;make [name] [content]`\n`;show [name]`\n`;edit [name] [content]`\n`;delete [name]`\n`;taglist`\n**Anything in [] is required. Anything in <> is optional.**"
        )
        page9 = Page(
            "**YashBot3001 Help**\nOther:\n`;bros`\n`;dyt`\n`;enigma`\n`;evrst`\n`;nerdstep`\n**Anything in [] is required. Anything in <> is optional.**"
        )
        root.link(
            page1,
            description="Fun",
            reaction="\U0001F3AE",
        )
        root.link(
            page2,
            description="Math",
            reaction="\U0001F522",
        )
        root.link(
            page3,
            description="Info",
            reaction="\U0001F5DE",
        )
        root.link(
            page4,
            description="Text Manipulation",
            reaction="\U0001F520",
        )
        root.link(
            page5,
            description="Image Manipulation",
            reaction="\U0001F5BC",
        )
        root.link(
            page6,
            description="Support Server Only",
            reaction="\U0001F6E0",
        )
        root.link(
            page7,
            description="Web",
            reaction="\U0001F4BB",
        )
        root.link(
            page8,
            description="Tags",
            reaction="\U0001F4CC",
        )
        root.link(
            page9,
            description="Other",
            reaction="\u2753",
        )
        h = Help(
            self.client,
            root,
        )
        await ctx.send(
            f"Check your DMs, {ctx.message.author.mention}!"
        )
        await h.display(
            ctx.message.author
        )

    @help.command()
    async def fun(
        self,
        ctx,
    ):
        root = Page(
            "These are all the commands in the `fun` category. Use the reactions to navigate."
        )
        page1 = Page(
            "`;8ball`\nAnswers your yes/no question."
        )
        page2 = Page(
            "`;fight <challenger1> <challenger2>`\nFights two people to the death!"
        )
        page3 = Page(
            "`;kill <target>/;bully <target>`\nKills/bullies your input."
        )
        page4 = Page(
            "`;rate <member>`\nRates you"
        )
        page5 = Page(
            "`;coin/;dice`\nFlips a coin/Rolls a dice"
        )
        page6 = Page(
            "`;cat/;dog/;hamster`\nSends you a cute GIF of a dog/cat/hamster"
        )
        page7 = Page(
            "`;thanos`\nDetermines whether or not you were killed in the Snap"
        )
        page8 = Page(
            "`;rps [choice]`\nRock Paper Scissors in Discord!"
        )
        page9 = Page(
            "`;hack <target>`\nHacks someone"
        )
        root.link(
            page1,
            description="8ball",
            reaction="1\N{combining enclosing keycap}",
        )
        root.link(
            page2,
            description="Fight",
            reaction="2\N{combining enclosing keycap}",
        )
        root.link(
            page3,
            description="Kill/Bully",
            reaction="3\N{combining enclosing keycap}",
        )
        root.link(
            page4,
            description="Rate",
            reaction="4\N{combining enclosing keycap}",
        )
        root.link(
            page5,
            description="Coin/Dice",
            reaction="5\N{combining enclosing keycap}",
        )
        root.link(
            page6,
            description="Dog/Cat/Hamster",
            reaction="6\N{combining enclosing keycap}",
        )
        root.link(
            page7,
            description="Thanos",
            reaction="7\N{combining enclosing keycap}",
        )
        root.link(
            page8,
            description="Rock Paper Scissors",
            reaction="8\N{combining enclosing keycap}",
        )
        root.link(
            page9,
            description="Hack",
            reaction="9\N{combining enclosing keycap}",
        )
        h = Help(
            self.client,
            root,
        )
        await ctx.send(
            f"Check your DMs, {ctx.message.author.mention}!"
        )
        await h.display(
            ctx.message.author
        )

    @help.command()
    async def math(
        self,
        ctx,
    ):
        root = Page(
            "These are all the commands in the `math` category. Use the reactions to navigate."
        )
        page1 = Page(
            "`;square [number]/;root [number]`\nSquares/Roots a number"
        )
        page2 = Page(
            "`;multiply [number1] [number2]`\nMultiplies a number"
        )
        page3 = Page(
            "`;factorial [number]`\nFinds the factorial of a number"
        )
        page4 = Page(
            "`;exp [number1] [number2]`\nnumber1 to the power of number2"
        )
        page5 = Page(
            "`;sine [number]/;cosine [number]/;tan [number]`\n sine/cosine/tangent of a number"
        )
        page6 = Page(
            "`;divide [number1] [number2]`\nDivides two numbers"
        )
        page7 = Page(
            "`;add [number1] [number2]/;subtract [number1] [number2]`\nAdds/Subtracts two numbers"
        )
        root.link(
            page1,
            description="Square/Root",
            reaction="1\N{combining enclosing keycap}",
        )
        root.link(
            page2,
            description="Multiply",
            reaction="2\N{combining enclosing keycap}",
        )
        root.link(
            page3,
            description="Factorial",
            reaction="3\N{combining enclosing keycap}",
        )
        root.link(
            page4,
            description="Exponent",
            reaction="4\N{combining enclosing keycap}",
        )
        root.link(
            page5,
            description="Sine/Cosine/Tangent",
            reaction="5\N{combining enclosing keycap}",
        )
        root.link(
            page6,
            description="Divide",
            reaction="6\N{combining enclosing keycap}",
        )
        root.link(
            page7,
            description="Add/Subtract",
            reaction="7\N{combining enclosing keycap}",
        )
        h = Help(
            self.client,
            root,
        )
        await ctx.send(
            f"Check your DMs, {ctx.message.author.mention}!"
        )
        await h.display(
            ctx.message.author
        )

    @help.command()
    async def info(
        self,
        ctx,
    ):
        root = Page(
            "These are all the commands in the `info` category. Use the reactions to navigate."
        )
        page1 = Page(
            "`;help <category>`\nSends this message"
        )
        page2 = Page(
            "`;info`\nSends info about the bot"
        )
        page3 = Page(
            "`;invite`\nSends an invite link to invite the bot"
        )
        page4 = Page(
            "`;source`\nSends a link to the GitHub repo"
        )
        page5 = Page(
            "`;uptime`\nSends the uptime"
        )
        root.link(
            page1,
            description="Help",
            reaction="1\N{combining enclosing keycap}",
        )
        root.link(
            page2,
            description="Info",
            reaction="2\N{combining enclosing keycap}",
        )
        root.link(
            page3,
            description="Invite",
            reaction="3\N{combining enclosing keycap}",
        )
        root.link(
            page4,
            description="Source",
            reaction="4\N{combining enclosing keycap}",
        )
        root.link(
            page5,
            description="Uptime",
            reaction="5\N{combining enclosing keycap}",
        )
        h = Help(
            self.client,
            root,
        )
        await ctx.send(
            f"Check your DMs, {ctx.message.auhtor.mention}!"
        )
        await h.display(
            ctx.message.author
        )

    @help.command()
    async def text(
        self,
        ctx,
    ):
        root = Page(
            "These are all the commands in the `text manipulation` category. Use the reactions to navigate."
        )
        page1 = Page(
            "`;secret <message>`\nTurns input into a ||spoiler||"
        )
        page2 = Page(
            ";echo <message>`\nRepeats input"
        )
        page3 = Page(
            "`;tts [message]`\nTurns your input into Text to Speech. Works best on computer."
        )
        page4 = Page(
            "`;embed <message>`\nTurns input into an embed"
        )
        page5 = Page(
            "`;ascii [message]`\nTurns your input into Ascii art. Works best on computer and with shorter messages.."
        )
        page6 = Page(
            "`;upper [message]/;lower [message]/;reverse [message]`\nCapitalizes/Lowercases/Reverses the input"
        )
        root.link(
            page1,
            description="Secret",
            reaction="1\N{combining enclosing keycap}",
        )
        root.link(
            page2,
            description="Echo",
            reaction="2\N{combining enclosing keycap}",
        )
        root.link(
            page3,
            description="Embed",
            reaction="3\N{combining enclosing keycap}",
        )
        root.link(
            page4,
            description="TTS",
            reaction="4\N{combining enclosing keycap}",
        )
        root.link(
            page5,
            description="ascii",
            reaction="5\N{combining enclosing keycap}",
        )
        root.link(
            page6,
            description="Upper/Lower/Reverse",
            reaction="6\N{combining enclosing keycap}",
        )
        h = Help(
            self.client,
            root,
        )
        await ctx.send(
            f"Check your DMs, {ctx.message.author.mention}!"
        )
        await h.display(
            ctx.message.author
        )

    @help.command()
    async def image(
        self,
        ctx,
    ):
        root = Page(
            "These are all the commands in the `image manipulation` category. Use the reactions to navigate."
        )
        page1 = Page(
            "`;kirby [message]`"
        )
        page2 = Page(
            "`;lisa [message]`"
        )
        page3 = Page(
            "`;pewds [message]`"
        )
        page4 = Page(
            "`;gru [message]`"
        )
        page5 = Page(
            "`;linus [message]`"
        )
        page6 = Page(
            "`;trump [message]`"
        )
        page7 = Page(
            "`;elon [message]`"
        )
        page8 = Page(
            "`;spongebob [message]`"
        )
        page9 = Page(
            "`;billboard [message]`"
        )
        page10 = Page(
            "`;supreme [message]`"
        )
        pagea = Page(
            "`;deepfry <member>`\nMakes your inputted member's avatar look 'deepfried'. Defaults to your own avatar if no member is given."
        )
        pageb = Page(
            "`;sad <member>`\nMakes your inputted member's avatar look sad. Defaults to your own avatar if no member is given."
        )
        pagec = Page(
            "`;emboss <member>`\nMakes your inputted member's avatar look like it has been embossed in stone. Defaults to your own avatar if no member is given."
        )
        paged = Page(
            "`;invert <member>`\nInverts your inputted member's avatar. Defaults to your own avatar if no member is given."
        )
        root.link(
            page1,
            description="Kirby",
            reaction="1\N{combining enclosing keycap}",
        )
        root.link(
            page2,
            description="Lisa",
            reaction="2\N{combining enclosing keycap}",
        )
        root.link(
            page3,
            description="Pewds",
            reaction="3\N{combining enclosing keycap}",
        )
        root.link(
            page4,
            description="Gru",
            reaction="4\N{combining enclosing keycap}",
        )
        root.link(
            page5,
            description="Linus",
            reaction="5\N{combining enclosing keycap}",
        )
        root.link(
            page6,
            description="Trump",
            reaction="6\N{combining enclosing keycap}",
        )
        root.link(
            page7,
            description="Elon",
            reaction="7\N{combining enclosing keycap}",
        )
        root.link(
            page8,
            description="Spongebob",
            reaction="8\N{combining enclosing keycap}",
        )
        root.link(
            page9,
            description="Billboard",
            reaction="9\N{combining enclosing keycap}",
        )
        root.link(
            page10,
            description="Supreme",
            reaction="\N{keycap ten}",
        )
        root.link(
            pagea,
            description="Deepfry",
            reaction="\U0001F1E6",
        )
        root.link(
            pageb,
            description="Sad",
            reaction="\U0001F1E7",
        )
        root.link(
            pagec,
            description="Emboss",
            reaction="\U0001F1E8",
        )
        root.link(
            paged,
            description="Invert",
            reaction="\U0001F1E9",
        )
        h = Help(
            self.client,
            root,
        )
        await ctx.send(
            f"Check your DMs, {ctx.message.author.mention}!"
        )
        await h.display(
            ctx.message.author
        )

    @help.command()
    async def web(
        self,
        ctx,
    ):
        root = Page(
            "These are all the commands in the `web` category. Use the reactions to navigate."
        )
        page1 = Page(
            "`;google [query]`\nSearches Google"
        )
        page2 = Page(
            "`;youtube [query]`\nSearches YouTube"
        )
        page3 = Page(
            "`;wiki [query]`\nSearches Wikipedia"
        )
        root.link(
            page1,
            description="Google",
            reaction="1\N{combining enclosing keycap}",
        )
        root.link(
            page2,
            description="YouTube",
            reaction="2\N{combining enclosing keycap}",
        )
        root.link(
            page3,
            description="Wikipedia",
            reaction="3\N{combining enclosing keycap}",
        )
        h = Help(
            self.client,
            root,
        )
        await ctx.send(
            f"Check your DMs, {ctx.message.author.mention}!"
        )
        await h.display(
            ctx.message.author
        )

    @help.command()
    async def tag(
        self,
        ctx,
    ):
        root = Page(
            "These are all the commands in the `tag` category. Use the reactions to navigate."
        )
        page1 = Page(
            "`;make [name] [content]`\nMakes a tag"
        )
        page2 = Page(
            "`;show [name]`\nShows a tag"
        )
        page3 = Page(
            "`;edit [name] [content]`\nEdits an existing tag"
        )
        page4 = Page(
            "`;delete [name]`\nDeletes an existing tag"
        )
        page5 = Page(
            "`;taglist`\nList of every tag"
        )
        root.link(
            page1,
            description="Make",
            reaction="1\N{combining enclosing keycap}",
        )
        root.link(
            page2,
            description="Show",
            reaction="2\N{combining enclosing keycap}",
        )
        root.link(
            page3,
            description="Edit",
            reaction="3\N{combining enclosing keycap}",
        )
        root.link(
            page4,
            description="Delete",
            reaction="4\N{combining enclosing keycap}",
        )
        root.link(
            page5,
            description="Taglist",
            reaction="5\N{combining enclosing keycap}",
        )
        h = Help(
            self.client,
            root,
        )
        await ctx.send(
            f"Check your DMs, {ctx.message.author.mention}!"
        )
        await h.display(
            ctx.message.author
        )


def setup(
    client
):
    client.add_cog(
        HelpCog(
            client
        )
    )
