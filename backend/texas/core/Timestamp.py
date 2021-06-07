#!/usr/bin/python
#-*- coding: utf-8 -*-

class Timestamp:
    def __init__(self):
        self._timestamp = None
        self._year = ""
        self._month = ""
        self._day = ""
        self._hour = ""
        self._minute = ""
        self._second = ""

    def setTimestamp(self, pTimestamp : str): # format 'YYYY-MM-DDTHH:mm:SS'
        self._timestamp = None
        self._year = None
        self._month = None
        self._day = None
        self._hour = None
        self._minute = None
        self._second = None
        if pTimestamp is not None:
            if len(pTimestamp) < 4 or (len(pTimestamp) > 4 and pTimestamp[4] != "-") or (len(pTimestamp) > 7 and pTimestamp[7] != "-") or (len(pTimestamp) > 10 and pTimestamp[10] != "T") or (len(pTimestamp) > 13 and pTimestamp[13] != ":") or (len(pTimestamp) > 16 and pTimestamp[16] != ":"):
               raise Exception("Invalid TimeML date/time format 'YYYY-MM-DDTHH:mm:SS' in '"+pTimestamp+"'");
            if len(pTimestamp) >= 4:
                self._year = pTimestamp[0:4]
            if len(pTimestamp) >= 7:
                self._month = pTimestamp[5:7]
                if self._month != "XX" and (int(self._month) < 1 or int(self._month) > 12):
                    raise Exception("Invalid month in '"+pTimestamp+"' (format 'YYYY-MM-DDTHH:mm:SS')")
            if len(pTimestamp) >= 10:
                self._day = pTimestamp[8:10]
                if self._day != "XX" and (int(self._day) < 1 or int(self._day) > 31):
                    raise Exception("Invalid day in '"+pTimestamp+"' (format 'YYYY-MM-DDTHH:mm:SS')")
            if len(pTimestamp) >= 13:
                self._hour = pTimestamp[11:13]
                if self._hour != "XX" and (int(self._hour) < 1 or int(self._hour) > 23):
                    raise Exception("Invalid hour in '"+pTimestamp+"' (format 'YYYY-MM-DDTHH:mm:SS')")
            if len(pTimestamp) >= 16:
                self._minute = pTimestamp[14:16]
                if self._minute != "XX" and (int(self._minute) < 0 or int(self._minute) > 59):
                    raise Exception("Invalid minute in '"+pTimestamp+"' (format 'YYYY-MM-DDTHH:mm:SS')")
            if len(pTimestamp) >= 19:
                self._second = pTimestamp[17:19]
                if self._second != "XX" and (int(self._second) < 0 or int(self._second) > 59):
                    raise Exception("Invalid second in '"+pTimestamp+"' (format 'YYYY-MM-DDTHH:mm:SS')")
            self._timestamp = self._year
            if self._month:
                self._timestamp += "-" + self._month
                if self._day:
                    self._timestamp += "-" + self._day
                    if self._hour:
                        self._timestamp += "T" + self._hour
                        if self._minute:
                            self._timestamp += ":" + self._minute
                            if self._second:
                                self._timestamp += ":" + self._second

    def getTimestamp(self):
        return self._timestamp
    def timestamp(self):
        return self._timestamp

    def getYear(self):
        return self._year
    def year(self):
        return self._year

    def getMonth(self):
        return self._month
    def month(self):
        return self._month

    def getDay(self):
        return self._day
    def day(self):
        return self._day

    def getHour(self):
        return self._hour
    def hour(self):
        return self._hour

    def getMinute(self):
        return self._minute
    def minute(self):
        return self._minute

    def getSecond(self):
        return self._second
    def second(self):
        return self._second

    def TAS(self, ):
        pass

    def isValid(self, raiseException : bool):
        pass

