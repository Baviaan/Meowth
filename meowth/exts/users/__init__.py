"""This cog contains features relating to Pokemon Go teams."""

from .users_cog import Users, MeowthUser

def setup(bot):
    bot.add_cog(Users(bot))