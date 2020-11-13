# Timespan
 CSS 340 Assignment 2: Class Design / Operator Overloads
    
    Purpose:
        This programming assignment will provide exercises in designing classes with proper
        abstraction and interfaces. Encapsulation and abstraction are key components of Python as
        well as OOP in general. The programming assignment will also require understanding of
        operator overloading   

    TimeSpan:
        Design and implement a TimeSpan class which represents a duration of time in seconds,
        minutes and hours. The order seconds, minutes, and hours should be respected in the
        constructor.
        
        As an example
            duration = TimeSpan(3, 2, 1);
        is a duration of time of 1 hour, 2 minutes and 3 seconds.
        
        You should store the values as integers in a normalized way but they may be passed in as floats.
        The stored number of seconds should be between -60 and 60; the stored number of minutes
        should be between -60 and 60. However, durations can be created with input arguments
        outside these ranges and you should normalize these. You do not need to worry about integer
        overflow for very big TimeSpans.
        
        As another example
            duration = TimeSpan(90, 2, 1);
        is stored as a duration of time of 1 hour, 3 minutes and 30 seconds.
        
        Accessor functions required
            The TimeSpan class should implement the following getters/setters:
                def getHours(): return the number of hours as an int
                def getMinutes(): return the number of minutes as an int
                def getSeconds(): return the number of Seconds as an int
                def setTime(seconds, minutes, hours): set the number of hours, minutes, seconds
        
        Constructor
            The class should define the constructor so that it can receive both floats and ints.
            However, the class stores the data as integers so rounding is required.
            TimeSpan(-10, 4, 1.5) represents 1 hour, 33 minutes, 50 seconds.
            If only one parameter is passed during initialization assume it is a second. If there are two
            assume seconds and minutes (in that order).
            TimeSpan(3, 67) represents 1 hour, 7 minutes, 3 seconds.
        
        Operators
            The class must overload and implement the following math operators: addition,
            subtraction, and Unary Negation. The class must make sure that += and -= assignment
            statements as well.
            The class must overload and implement the full set of equivalence and comparator
            operations. For instance, ==, <, <=, etc.
        
        I/O
            The class must print out a useful representation of itself when passed to the print
            function.
            Output
            For formatting use the following:
                duration = TimeSpan(1,2,3)
                print(duration)
            Should output:
                Hours: 3, Minutes: 2, Seconds: 1
            Please use this EXACT format.

        Grade:
        41.5 / 50
         -1.0: Fuller set of verbs, such as changeAvailable
         -2.0: No comments
         -5.5: normalization errors
