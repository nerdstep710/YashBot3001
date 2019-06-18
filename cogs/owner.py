import discord
from discord.ext import (
    commands,
)


def is_me():
    def predicate(
        ctx
    ):
        return (
            ctx.message.author.id
            == 530064431909175346
        )

    return commands.check(
        predicate
    )


class OwnerCog(
    commands.Cog
):
    def __init__(
        self,
        client,
    ):
        self.client = client

    @commands.command()
    @is_me()
    async def test(
        self,
        ctx,
    ):
        channel = self.client.get_channel(
            577195540165558350
        )
        name = (
            ctx.message.author.display_name
        )
        avy = (
            ctx.message.author.avatar
        )
        print(
            f"Test successful for {name}"
        )
        await channel.send(
            avy
        )
        await channel.send(
            f"Test successful for {name}"
        )

    # must be used in the guild the channel belongs to.
    @commands.command()
    @is_me()
    async def poll(
        self,
        ctx,
        *,
        question="",
    ):
        channel = self.client.get_channel(
            579317022740185098
        )
        role = discord.utils.get(
            ctx.message.guild.roles,
            name="Polls",
        )
        message = await channel.send(
            f"{role.mention} {question}"
        )
        await message.add_reaction(
            "\U0001F44D"
        )
        await message.add_reaction(
            "\U0001F44E"
        )


def setup(
    client
):
    client.add_cog(
        OwnerCog(
            client
        )
    )
