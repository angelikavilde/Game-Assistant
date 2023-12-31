"""Rock-Paper-Scissors event functions"""

from discord import Interaction, ButtonStyle
from discord.ui import button, Button, View


async def check_rps_played(interaction: Interaction) -> bool:
    """Verifies the event's activation status to make sure event can be played"""
    from bot import bot_message
    if not bot_message or "chose" not in str(bot_message.content):
        return False
    await interaction.response.send_message("`Re-start the game!`")
    return True


def who_won_rps(bot_chose: str, user_chose: str) -> str:
    """Returns text on who chose what and who won/lost"""
    if bot_chose == user_chose:
        return f"`I also chose {bot_chose}. We tie!`"
    if (user_chose,bot_chose) in [("scissors","rock"),("rock","paper"),("paper","scissors")]:
        return f"`I chose {bot_chose}. You lose!`"
    return f"`I chose {bot_chose}. You win!`"


class RockPaperScissors(View):
    """Class for rock paper scissors buttons"""

    def __init__(self, bot_choice: str):
        super().__init__(timeout=10)
        self.bot_choice = bot_choice

    @button(label="Rock", row=0, style=ButtonStyle.red)
    async def rock(self, interaction: Interaction, Button: Button) -> None:
        """User clicked rock button"""
        if not await check_rps_played(interaction):
            await interaction.response.send_message(who_won_rps(self.bot_choice, "rock"))

    @button(label="Paper", row=0, style=ButtonStyle.red)
    async def paper(self, interaction: Interaction, Button: Button) -> None:
        """User clicked paper button"""
        if not await check_rps_played(interaction):
            await interaction.response.send_message(who_won_rps(self.bot_choice, "paper"))

    @button(label="Scissors", row=0, style=ButtonStyle.red)
    async def scissors(self, interaction: Interaction, Button: Button) -> None:
        """User clicked scissors button"""
        if not await check_rps_played(interaction):
            await interaction.response.send_message(who_won_rps(self.bot_choice, "scissors"))
