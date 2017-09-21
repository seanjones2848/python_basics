# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex00.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sjones <sjones@student.42.us.org>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/09/21 14:52:09 by sjones            #+#    #+#              #
#    Updated: 2017/09/21 14:53:48 by sjones           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

if hasattr(__builtins__, 'raw_input'):
	input=raw_input

name = str(input("Hello hacker, what is your name?\n"));
print("Welcome, " + name);
