#!/usr/bin/env python
# -*- coding:utf-8 -*-

# import shlex
import os,sys
import urllib
import urllib2
import re
import Image
import cookielib

def todict(str0):
    totalCount="totalCount"
    success="success"
    msg="msg"
    singleInfo="singleInfo"
    data="data"
    SchDate="SchDate"
    SchGlobalCode="SchGlobalCode"
    SchLocalCode="SchLocalCode"
    SchLineName="SchLineName"
    SchStationCode="SchStationCode"
    SchStationName="SchStationName"
    SchCompCode="SchCompCode"
    SchCompName="SchCompName"
    SchBusBrand="SchBusBrand"
    SchBusBrandColor="SchBusBrandColor"
    SchTime="SchTime"
    SchWaitingRoom="SchWaitingRoom"
    SchCheckGate="SchCheckGate"
    SchBerth="SchBerth"
    SchType="SchType"
    SchMode="SchMode"
    SchDstCity="SchDstCity"
    SchDstNode="SchDstNode"
    SchDstNodeName="SchDstNodeName"
    SchOperType="SchOperType"
    SchFirstTime="SchFirstTime"
    SchLastTime="SchLastTime"
    SchInterval="SchInterval"
    SchNodeNameList="SchNodeNameList"
    SchDist="SchDist"
    SchSeatCount="SchSeatCount"
    SchPrice="SchPrice"
    SchDiscPrice="SchDiscPrice"
    SchStdPrice="SchStdPrice"
    SchFuel="SchFuel"
    SchBusType="SchBusType"
    SchBusLevel="SchBusLevel"
    SchTicketCount="SchTicketCount"
    SchChild="SchChild"
    SchStat="SchStat"
    SchPrintSeat="SchPrintSeat"
    Notes="Notes"
    SchNodeName="SchNodeName"
    SchNodeCode="SchNodeCode"
    
    return eval(str0)



    

if __name__ == '__main__' :
  print 1111
#     todict(str0='totalCount:13,success:"true",msg:"",singleInfo:"",data:""')
  print todict(str0=u'{totalCount:13,success:"true",msg:"",singleInfo:"",data:[{SchDate:"2016-03-19",SchGlobalCode:"",SchLocalCode:"30008",SchLineName:"打通",SchStationCode:"6001",SchStationName:"重庆南坪汽车站",SchCompCode:"",SchCompName:"",SchBusBrand:"",SchBusBrandColor:"",SchTime:"07:10",SchWaitingRoom:"4",SchCheckGate:"4号",SchBerth:"",SchType:"始发",SchMode:"普通",SchDstCity:"",SchDstNode:"dxa",SchDstNodeName:"打通",SchOperType:"",SchFirstTime:"",SchLastTime:"",SchInterval:"0",SchNodeNameList:"赶水",SchDist:"134.00",SchSeatCount:"38",SchPrice:"49.00",SchDiscPrice:"25.00",SchStdPrice:"49.00",SchFuel:"5.50",SchBusType:"中高一级",SchBusLevel:"",SchTicketCount:"38",SchChild:"3",SchStat:"1",SchPrintSeat:"1",Notes:"",SchNodeName:"打通",SchNodeCode:"dt"},{SchDate:"2016-03-19",SchGlobalCode:"",SchLocalCode:"30006",SchLineName:"打通",SchStationCode:"6001",SchStationName:"重庆南坪汽车站",SchCompCode:"",SchCompName:"",SchBusBrand:"",SchBusBrandColor:"",SchTime:"07:50",SchWaitingRoom:"4",SchCheckGate:"4号",SchBerth:"",SchType:"始发",SchMode:"普通",SchDstCity:"",SchDstNode:"dxa",SchDstNodeName:"打通",SchOperType:"",SchFirstTime:"",SchLastTime:"",SchInterval:"0",SchNodeNameList:"赶水",SchDist:"134.00",SchSeatCount:"38",SchPrice:"49.00",SchDiscPrice:"25.00",SchStdPrice:"49.00",SchFuel:"5.50",SchBusType:"中高一级",SchBusLevel:"",SchTicketCount:"38",SchChild:"3",SchStat:"1",SchPrintSeat:"1",Notes:"",SchNodeName:"打通",SchNodeCode:"dt"},{SchDate:"2016-03-19",SchGlobalCode:"",SchLocalCode:"30001",SchLineName:"打通",SchStationCode:"6001",SchStationName:"重庆南坪汽车站",SchCompCode:"",SchCompName:"",SchBusBrand:"",SchBusBrandColor:"",SchTime:"08:50",SchWaitingRoom:"4",SchCheckGate:"4号",SchBerth:"",SchType:"始发",SchMode:"普通",SchDstCity:"",SchDstNode:"dxa",SchDstNodeName:"打通",SchOperType:"",SchFirstTime:"",SchLastTime:"",SchInterval:"0",SchNodeNameList:"赶水",SchDist:"134.00",SchSeatCount:"38",SchPrice:"49.00",SchDiscPrice:"25.00",SchStdPrice:"49.00",SchFuel:"5.50",SchBusType:"中高一级",SchBusLevel:"",SchTicketCount:"38",SchChild:"3",SchStat:"1",SchPrintSeat:"1",Notes:"",SchNodeName:"打通",SchNodeCode:"dt"},{SchDate:"2016-03-19",SchGlobalCode:"",SchLocalCode:"30010",SchLineName:"打通",SchStationCode:"6001",SchStationName:"重庆南坪汽车站",SchCompCode:"",SchCompName:"",SchBusBrand:"",SchBusBrandColor:"",SchTime:"09:50",SchWaitingRoom:"4",SchCheckGate:"4号",SchBerth:"",SchType:"始发",SchMode:"普通",SchDstCity:"",SchDstNode:"dxa",SchDstNodeName:"打通",SchOperType:"",SchFirstTime:"",SchLastTime:"",SchInterval:"0",SchNodeNameList:"赶水",SchDist:"134.00",SchSeatCount:"38",SchPrice:"49.00",SchDiscPrice:"25.00",SchStdPrice:"49.00",SchFuel:"5.50",SchBusType:"中高一级",SchBusLevel:"",SchTicketCount:"38",SchChild:"3",SchStat:"1",SchPrintSeat:"1",Notes:"",SchNodeName:"打通",SchNodeCode:"dt"},{SchDate:"2016-03-19",SchGlobalCode:"",SchLocalCode:"30007",SchLineName:"打通",SchStationCode:"6001",SchStationName:"重庆南坪汽车站",SchCompCode:"",SchCompName:"",SchBusBrand:"",SchBusBrandColor:"",SchTime:"10:30",SchWaitingRoom:"4",SchCheckGate:"4号",SchBerth:"",SchType:"始发",SchMode:"普通",SchDstCity:"",SchDstNode:"dxa",SchDstNodeName:"打通",SchOperType:"",SchFirstTime:"",SchLastTime:"",SchInterval:"0",SchNodeNameList:"赶水",SchDist:"134.00",SchSeatCount:"38",SchPrice:"49.00",SchDiscPrice:"25.00",SchStdPrice:"49.00",SchFuel:"5.50",SchBusType:"中高一级",SchBusLevel:"",SchTicketCount:"38",SchChild:"3",SchStat:"1",SchPrintSeat:"1",Notes:"",SchNodeName:"打通",SchNodeCode:"dt"},{SchDate:"2016-03-19",SchGlobalCode:"",SchLocalCode:"30003",SchLineName:"打通",SchStationCode:"6001",SchStationName:"重庆南坪汽车站",SchCompCode:"",SchCompName:"",SchBusBrand:"",SchBusBrandColor:"",SchTime:"11:00",SchWaitingRoom:"4",SchCheckGate:"4号",SchBerth:"",SchType:"始发",SchMode:"普通",SchDstCity:"",SchDstNode:"dxa",SchDstNodeName:"打通",SchOperType:"",SchFirstTime:"",SchLastTime:"",SchInterval:"0",SchNodeNameList:"赶水",SchDist:"134.00",SchSeatCount:"38",SchPrice:"49.00",SchDiscPrice:"25.00",SchStdPrice:"49.00",SchFuel:"5.50",SchBusType:"中高一级",SchBusLevel:"",SchTicketCount:"38",SchChild:"3",SchStat:"1",SchPrintSeat:"1",Notes:"",SchNodeName:"打通",SchNodeCode:"dt"},{SchDate:"2016-03-19",SchGlobalCode:"",SchLocalCode:"30012",SchLineName:"打通",SchStationCode:"6001",SchStationName:"重庆南坪汽车站",SchCompCode:"",SchCompName:"",SchBusBrand:"",SchBusBrandColor:"",SchTime:"11:30",SchWaitingRoom:"4",SchCheckGate:"4号",SchBerth:"",SchType:"始发",SchMode:"普通",SchDstCity:"",SchDstNode:"dxa",SchDstNodeName:"打通",SchOperType:"",SchFirstTime:"",SchLastTime:"",SchInterval:"0",SchNodeNameList:"赶水",SchDist:"134.00",SchSeatCount:"38",SchPrice:"49.00",SchDiscPrice:"25.00",SchStdPrice:"49.00",SchFuel:"5.50",SchBusType:"中高一级",SchBusLevel:"",SchTicketCount:"38",SchChild:"3",SchStat:"1",SchPrintSeat:"1",Notes:"",SchNodeName:"打通",SchNodeCode:"dt"},{SchDate:"2016-03-19",SchGlobalCode:"",SchLocalCode:"30013",SchLineName:"打通",SchStationCode:"6001",SchStationName:"重庆南坪汽车站",SchCompCode:"",SchCompName:"",SchBusBrand:"",SchBusBrandColor:"",SchTime:"12:20",SchWaitingRoom:"4",SchCheckGate:"4号",SchBerth:"",SchType:"始发",SchMode:"普通",SchDstCity:"",SchDstNode:"dxa",SchDstNodeName:"打通",SchOperType:"",SchFirstTime:"",SchLastTime:"",SchInterval:"0",SchNodeNameList:"赶水",SchDist:"134.00",SchSeatCount:"38",SchPrice:"49.00",SchDiscPrice:"25.00",SchStdPrice:"49.00",SchFuel:"5.50",SchBusType:"中高一级",SchBusLevel:"",SchTicketCount:"38",SchChild:"3",SchStat:"1",SchPrintSeat:"1",Notes:"",SchNodeName:"打通",SchNodeCode:"dt"},{SchDate:"2016-03-19",SchGlobalCode:"",SchLocalCode:"30015",SchLineName:"打通",SchStationCode:"6001",SchStationName:"重庆南坪汽车站",SchCompCode:"",SchCompName:"",SchBusBrand:"",SchBusBrandColor:"",SchTime:"13:30",SchWaitingRoom:"4",SchCheckGate:"4号",SchBerth:"",SchType:"始发",SchMode:"普通",SchDstCity:"",SchDstNode:"dxa",SchDstNodeName:"打通",SchOperType:"",SchFirstTime:"",SchLastTime:"",SchInterval:"0",SchNodeNameList:"赶水",SchDist:"134.00",SchSeatCount:"38",SchPrice:"49.00",SchDiscPrice:"25.00",SchStdPrice:"49.00",SchFuel:"5.50",SchBusType:"中高一级",SchBusLevel:"",SchTicketCount:"38",SchChild:"3",SchStat:"1",SchPrintSeat:"1",Notes:"",SchNodeName:"打通",SchNodeCode:"dt"},{SchDate:"2016-03-19",SchGlobalCode:"",SchLocalCode:"30002",SchLineName:"打通",SchStationCode:"6001",SchStationName:"重庆南坪汽车站",SchCompCode:"",SchCompName:"",SchBusBrand:"",SchBusBrandColor:"",SchTime:"14:30",SchWaitingRoom:"4",SchCheckGate:"4号",SchBerth:"",SchType:"始发",SchMode:"普通",SchDstCity:"",SchDstNode:"dxa",SchDstNodeName:"打通",SchOperType:"",SchFirstTime:"",SchLastTime:"",SchInterval:"0",SchNodeNameList:"赶水",SchDist:"134.00",SchSeatCount:"38",SchPrice:"49.00",SchDiscPrice:"25.00",SchStdPrice:"49.00",SchFuel:"5.50",SchBusType:"中高一级",SchBusLevel:"",SchTicketCount:"38",SchChild:"3",SchStat:"1",SchPrintSeat:"1",Notes:"",SchNodeName:"打通",SchNodeCode:"dt"},{SchDate:"2016-03-19",SchGlobalCode:"",SchLocalCode:"30020",SchLineName:"打通",SchStationCode:"6001",SchStationName:"重庆南坪汽车站",SchCompCode:"",SchCompName:"",SchBusBrand:"",SchBusBrandColor:"",SchTime:"15:30",SchWaitingRoom:"4",SchCheckGate:"4号",SchBerth:"",SchType:"始发",SchMode:"普通",SchDstCity:"",SchDstNode:"dxa",SchDstNodeName:"打通",SchOperType:"",SchFirstTime:"",SchLastTime:"",SchInterval:"0",SchNodeNameList:"赶水",SchDist:"134.00",SchSeatCount:"38",SchPrice:"49.00",SchDiscPrice:"25.00",SchStdPrice:"49.00",SchFuel:"5.50",SchBusType:"中高一级",SchBusLevel:"",SchTicketCount:"38",SchChild:"3",SchStat:"1",SchPrintSeat:"1",Notes:"",SchNodeName:"打通",SchNodeCode:"dt"},{SchDate:"2016-03-19",SchGlobalCode:"",SchLocalCode:"30009",SchLineName:"打通",SchStationCode:"6001",SchStationName:"重庆南坪汽车站",SchCompCode:"",SchCompName:"",SchBusBrand:"",SchBusBrandColor:"",SchTime:"17:30",SchWaitingRoom:"4",SchCheckGate:"4号",SchBerth:"",SchType:"始发",SchMode:"普通",SchDstCity:"",SchDstNode:"dxa",SchDstNodeName:"打通",SchOperType:"",SchFirstTime:"",SchLastTime:"",SchInterval:"0",SchNodeNameList:"赶水",SchDist:"134.00",SchSeatCount:"38",SchPrice:"49.00",SchDiscPrice:"25.00",SchStdPrice:"49.00",SchFuel:"5.50",SchBusType:"中高一级",SchBusLevel:"",SchTicketCount:"38",SchChild:"3",SchStat:"1",SchPrintSeat:"1",Notes:"",SchNodeName:"打通",SchNodeCode:"dt"},{SchDate:"2016-03-19",SchGlobalCode:"",SchLocalCode:"30027",SchLineName:"打通",SchStationCode:"6001",SchStationName:"重庆南坪汽车站",SchCompCode:"",SchCompName:"",SchBusBrand:"",SchBusBrandColor:"",SchTime:"18:30",SchWaitingRoom:"4",SchCheckGate:"4号",SchBerth:"",SchType:"始发",SchMode:"普通",SchDstCity:"",SchDstNode:"dxa",SchDstNodeName:"打通",SchOperType:"",SchFirstTime:"",SchLastTime:"",SchInterval:"0",SchNodeNameList:"赶水",SchDist:"134.00",SchSeatCount:"38",SchPrice:"49.00",SchDiscPrice:"25.00",SchStdPrice:"49.00",SchFuel:"5.50",SchBusType:"中高一级",SchBusLevel:"",SchTicketCount:"38",SchChild:"3",SchStat:"1",SchPrintSeat:"1",Notes:"",SchNodeName:"打通",SchNodeCode:"dt"}]}')
