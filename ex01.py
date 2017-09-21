# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex01.py2                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sjones <sjones@student.42.us.org>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/09/21 14:41:30 by sjones            #+#    #+#              #
#    Updated: 2017/09/21 14:48:46 by sjones           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

if hasattr(__builtins__, 'raw_input'):
	input=raw_input

name = str(input("Who goes there?\n"));

if name == "DHTFHNUQARFMQMKGSPRLRSKBCMD":
	print("Welcome Daenerys.");
elif name == "Dany":
	print("Dany who?");
else:
	print("Move along, now.");

