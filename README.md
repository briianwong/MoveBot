MOVEBOT for Discord
by Brian Wong

What is this:
This is a text-based Discord bot used to move multiple users around different voice channels at the same time.

MoveBot currently has 3 functions: move entire channel, move mentioned users, and team split voice call.

1. Move Channel
This command takes 2 parameters, first being the initial channel, and second being the destination channel. This will move all users connected to the initial channel to the destination channel.
To use this command, type !movec 'initialChannel' 'destinationChannel' . Where initialChannel and destinationChannel are the names of your channels.

2. Move Users
This command takes an undefined amount of parameters. This will move all mentioned users to the destination channel regardless of which channel they are currently apart of.
To use this command, type !moveu '@user1 @user2 @user3...' 'destinationChannel' . Where @user1 is the members username and destinationChannel is the name of the channel you want to move the users to.

3. Voice Team Split / 10-mans
This command takes 2 parameters, first being Team 1's voice channel, and second being Team 2's voice channel.
This will send a message which contains 3 buttons. The first 2 buttons assign the members who click a team while the 3 button moves the respective users into their team's channel.
To use this command, type !ten 'team1Channel' 'team2Channel' . Once everyone has clicked their team, one person can press start and the users will be moved.


How to add this to your own server:
Follow this guide: https://www.ionos.com/digitalguide/server/know-how/creating-discord-bot/
and
A tokenKey.py file which contains the token key of your bot.