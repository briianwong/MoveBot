MoveBot for Discord
by Brian Wong

What is this:
This is a text-based Discord bot used to move multiple users around different voice channels at the same time.

MoveBot currently has 3 functions: move entire channel, move mentioned users, and team split.

1. Move Channel: 
This command takes 2 parameters, first being the initial channel, and second being the destination channel. This will move all users connected to the initial channel to the destination channel.
To use this command, type !movec 'initialChannel' 'destinationChannel' . Where initialChannel and destinationChannel are the names of your channels.

Example of Move Channel:

![image](https://user-images.githubusercontent.com/80365798/224405969-da85701a-6f85-4658-a8ac-5e9d8dfa8241.png)


2. Move Users:
This command takes an undefined amount of parameters. This will move all mentioned users to the destination channel regardless of which channel they are currently apart of.
To use this command, type !moveu '@user1 @user2 @user3...' 'destinationChannel' . Where @user1 is the members username and destinationChannel is the name of the channel you want to move the users to.

Example of Move Users:

![image](https://user-images.githubusercontent.com/80365798/224406161-a4becd3e-f86d-4f9c-a7f9-29a8c17c6ede.png)


3. Team Split / 10-mans:
This command takes 2 parameters, first being Team 1's voice channel, and second being Team 2's voice channel.
This will send a message which contains 3 buttons. The first 2 buttons assign the members who click a team while the 3rd Start button moves all the respective users into their team's channel at the same time.
To use this command, type !ten 'team1Channel' 'team2Channel' . Once everyone has clicked their team, one person can press start and all members will be moved.

Example of Team Split / 10-mans:

![image](https://user-images.githubusercontent.com/80365798/224405765-1de9122f-5443-4bc1-a1a6-4d8142a50682.png)


How to add this to your own server:

Follow this guide: https://www.ionos.com/digitalguide/server/know-how/creating-discord-bot/
and create a new tokenKey.py file which contains the token key of your bot.
