from random import *
from turtle import *
import math


# this is my library and i try to add my useful codes here. maybe i can use it in the future

class graphics:
    # this class contains all functions related to turtle library like drawing shapes or creating patterns in turtle.

    def turtle_shape_draw(self, side_length):
        """
        this function takes two arguments and then draws a shape in turtle using them
        both arguments are integers
        first argument indicates the number of sides of that shape (for example, 3 means a triangle)
        second argument indicates the length of the shapes each side.
        """
        for i in range(self):
            forward(side_length)
            left(360 / self)


class in_out:
    # this class has all the algorithms related to strings, lists... such as generating tokens or detecting palindromes.

    uppercases = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O",
                  "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    # this is a list of uppercase letters

    lowercases = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
                  "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    # this is a list of lowercase letters

    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    # this is a list of numbers.

    def sort_it(self):
        """
        this function takes one list as its only argument
        the list should only contain numbers (integers, floats, ect...)
        then, this function sorts the numbers inside the list from the biggest to the smallest
        and returns a new sorted list.
        example:

        input: [54, 73, 23, 123, 6]       output: [123, 73, 54, 23, 6]
        """
        for i in range(len(self)):
            self[i] = int(self[i])
        progress = self.copy()
        self.clear()
        delete = []
        for i in range(len(progress)):
            delete.clear()
            while not len(progress) == 1:
                if progress[0] > progress[1]:
                    delete.append(progress[1])
                    progress.pop(1)
                else:
                    delete.append(progress[0])
                    progress.pop(0)
            self.append(progress[0])
            progress.clear()
            progress = delete.copy()
        return self

    def list_to_string(self):
        """
        this function takes one list as its only argument
        then, it turns the list into an string and returns the string
        example:

        input: [tr, tg, 65, 43]       output: "trtg6543"

        input: [5693, hi, hello, goodbye, 901]        output: "5693hihellogoodbye901"
        """
        result = ""
        for i in self:
            result += str(i)
        return result

    def detect_palindrome(self):
        """
        this function takes one argument which is a string.
        then, it returns True in case the word is a palindrome, otherwise, it returns False
        A palindrome is a word, number, phrase, or other sequence of symbols that reads the same backwards as forwards
        example:

        input: "wow"     output: True

        input: "hello"   output: False
        """
        result = True
        for i in range(round(len(self) / 2)):
            if not (self[i] == self[-(i + 1)]):
                result = False
                break
        return result

    def separate(self, separator):
        """
        this function takes two arguments.
        the first argument is a String with a set of words or phrases separated with comas, periods...
        the function then separates these words or phrases and returns them separately as a list
        what the words are separated with (comas, periods...) is chosen by the second argument.
        the separator must be only one character.
        example:

        input: "hello. goodbye. hey", "."     output: [hello, goodbye, hey]
        """
        current_word = ""
        complete_list = []
        for i in range(len(self)):
            if not self[i] == separator:
                current_word += self[i]
            else:
                complete_list.append(current_word)
                current_word = ""
        complete_list.append(current_word)
        return complete_list

    def generate_token(self):
        """
        this function takes one argument which should be an integer.
        it then generates a token (a random code) as long as the input integer.
        example:

        input: 5    output: "Tk8r2"

        input: 10   output: "96hkG5W30n"

        the token contains numbers, lowercase and uppercase letters.
        """
        alphabet_list = in_out.lowercases
        tokenASlist = []
        for x in range(self):
            nvl = randrange(0, 2)
            if nvl == 0:
                uol = randrange(0, 2)
                if uol == 0:
                    mm = alphabet_list[randrange(1, 26)]
                    tokenASlist.append(mm.upper())
                else:
                    tokenASlist.append(alphabet_list[randrange(1, 26)])
            else:
                tokenASlist.append(str(randrange(0, 10)))

        return in_out.list_to_string(tokenASlist)

    def detect_repeat(self, repeat_of):
        """
        this function takes two arguments
        first argument should be a string, same for the second argument.
        then, the function returns how many times the second argument has been repeated in the first argument.
        example:

        input: "hello", "ll"     output: 1

        input: "ramara", "ra"    output: 2
        """
        times = 0
        for i in range(len(self) - len(repeat_of) + 1):
            if self[i: i + len(repeat_of)] == repeat_of:
                times += 1
        return times

    def detect_prime(self):
        """
        this function takes one integer as its argument.
        then, it returns True if the integer is a prime number, otherwise, it returns False
        example:

        input: 13      output: True

        input: 21      output: False
        """
        # the following code is because the algorithm doesn't function properly for 1 and 2
        if self == 2:
            return True
        if self == 1:
            return False
        # the algorithm starts here
        max = math.trunc(math.sqrt(self))
        prime_no_list = [2]
        for i in range(2, max + 1):
            prime_no = True
            for ii in prime_no_list:
                if i % ii == 0:
                    prime_no = False
            if prime_no:
                prime_no_list.append(i)
        # now we have a list of prime numbers self shouldn't be dividable by
        for i in prime_no_list:
            if self % i == 0:
                return False
        return True

    def biggest_palindrome(self):
        """
        this function takes an string as its only argument.
        then, it returns the biggest palindrome existing in the string.
        A palindrome is a word, number, phrase, or other sequence of symbols that reads the same backwards as forwards.
        example:

        input: "lrkgrtghthgracecarhhh"      output: "racecar"
        """
        palindrome_list = []
        for dig in range(1, len(self) + 1):
            count = 0
            for count in range(len(self) - count + 1):
                if in_out.detect_palindrome(self[count: dig]) and len(self[count: dig]) > 1:
                    palindrome_list.append(self[count: dig])
        if not palindrome_list:
            return False
        else:
            return in_out.list_biggest(palindrome_list)

    def list_biggest(self):
        """
        this function takes one list as its only argument.
        then, it finds the longest item in the list and returns it.
        the list can contain anything including strings, integers, etc...
        example:

        input: ["hello", 90, "goodbye"]      output: "goodbye"

        input: [911, "google", "right", "apple"]      output: "google"
        """
        longest = ""
        for i in range(len(self)):
            if len(str(self[i])) > len(longest):
                longest = str(self[i])
        return longest

    def list_contain(self, item):
        """
        this function checks if a list contains the specified item or not.
        the first argument is the list, the second is the item you want to check.
        if the list contains the item, it will return True, otherwise, it returns False.
        example:

        input: ["apple", "banana", "blueberry", "orange"], "banana"      output: True

        input: ["cherry", "grapes", "peach", "cucumber"], "kiwi"      output: False
        """
        result = False
        for i in self:
            if i == item:
                result = True
        return result

    def check_allowed(self, *allow):
        """
        this function takes an input (an string) and checks if it contains illegal characters.
        you choose what is legal by the next arguments.
        you can write the following to indicate letters, numbers... and/or you could write characters separately.
        "lowercase", "uppercase", "number"
        returns True if no illegal characters, otherwise, returns False.
        example:

        input: self = "hello", "lowercase", "_", "$"      output: True

        input: self = "good90good", "number", "#"         output: False
        """
        raw_allowed = list(allow)
        allowed = []
        if in_out.list_contain(raw_allowed, "lowercase"):
            allowed.extend(in_out.lowercases)
            raw_allowed.remove("lowercase")
        if in_out.list_contain(raw_allowed, "uppercase"):
            allowed.extend(in_out.uppercases)
            raw_allowed.remove("uppercase")
        if in_out.list_contain(raw_allowed, "number"):
            allowed.extend(in_out.numbers)
            raw_allowed.remove("number")
        allowed.extend(raw_allowed)

        # from this point, we have the allowed list which contains all the allowed characters.
        result = True
        for i in range(len(self)):
            if not in_out.list_contain(allowed, self[i]):
                result = False
        return result

    def string_division(self, by=1):
        """
        this function takes an string (first argument) and divides it into pieces and returns it as a list.
        the second argument decides how many character by character to divide the string by.
        if a character or a few characters are left in the end that aren't dividable, they will be omitted.
        example:

        input: "hellofromme", 2      output: ["he", "ll", "of", "ro", "mm"]
        in the above example, the e in the end was omitted because of not being dividable.

        input: "apleasingday", 3      output: ["apl", "eas", "ing", "day"]
        """
        result = []
        for i in range(int(len(self) / by)):
            result.append(self[i * by: i * by + by])
        return result

    def string_positions(self, item):
        """
        this function takes an string and a character.
        then, it returns a set of numbers containing what indexes of the string contain that character.
        example:

        input: "hello", "l"      output: {2, 3}

        input: "apple and banana", "n"      output: {7, 12, 14}
        """
        result = set()
        for i in range(len(self)):
            if self[i] == item:
                result.add(i)
        return result

    def __alph_compare(word1, word2):
        """
        this function takes two string(words) and compares them to see which is greater in the alphabetic order
        then, the function returns 1 if word1 is greater and returns 2 if word2 is greater.

        notes:
        the function is not sensitive to uppercase and lowercase letters.
        numbers are prioritized compared to letters.
        space is prioritized compared to letters and numbers.
        characters other than numbers, letters and space are unrecognized and may cause errors.

        example:

        input: "hello", "zoo"        output: 1

        input: "anna", "amy"        output: 2
        """
        pri_list = [" "]
        pri_list += in_out.numbers
        pri_list += in_out.lowercases
        first_word = word1.lower()
        second_word = word2.lower()
        if len(first_word) < len(second_word):
            temp = first_word
            first_word = second_word
            second_word = temp
            swapped = True
        else:
            swapped = False
        first_word = in_out.string_division(first_word)
        second_word = in_out.string_division(second_word)
        for i in range(len(second_word)):
            if pri_list.index(second_word[i]) > pri_list.index(first_word[i]):
                if swapped:
                    return 2
                else:
                    return 1
            if pri_list.index(first_word[i]) > pri_list.index(second_word[i]):
                if swapped:
                    return 1
                else:
                    return 2
        if swapped:
            return 1
        else:
            return 2

    def alphabetical_sort(self):
        """
        this function takes a list full of strings as its input
        then, it sorts the list in alphabetical order and returns it.

        notes:
        the function is not sensitive to uppercase and lowercase letters.
        numbers are prioritized compared to letters.
        space is prioritized compared to letters and numbers.
        characters other than numbers, letters and space are unrecognized and may cause errors.
        all items of the list must be strings.

        example:

        input: ["zoo", "apple", "banana", "animals"]        output: ["animals", "apple", "banana", "zoo"]

        input: ["python", "is", "great"]        output: ["great", "is", "python"]
        """
        progress = self.copy()
        self.clear()
        delete = []
        for i in range(len(progress)):
            delete.clear()
            while not len(progress) == 1:
                if in_out.__alph_compare(progress[0], progress[1]) == 1:
                    delete.append(progress[1])
                    progress.pop(1)
                else:
                    delete.append(progress[0])
                    progress.pop(0)
            self.append(progress[0])
            progress.clear()
            progress = delete.copy()
        return self

    def thousands_separate(self):
        """
        this function takes an integer or string only containing numbers as input.
        then, it returns an string with the number separated by commas. (every three digits)

        example:

        input: 1239562        output: "1,239,562"

        input: "-8763"        output: "-8,763"
        """
        # we turn the integer/string into a list
        number = str(self)
        number = in_out.string_division(number, 1)
        # we remove the minus in case there is one, and set the variable neg to True in order to add the minus in the end
        neg = False
        if number[0] == "-":
            number.pop(0)
            neg = True
        # now, the algorithm starts
        final_number = ""
        for i in range(1, len(number)+1):
            if i % 3 == 0 and i != len(number):
                final_number = "," + number[-i] + final_number
            else:
                final_number = number[-i] + final_number
        # now we add a minus if existed in the first place and return the values
        if neg:
            return "-" + final_number
        else:
            return final_number