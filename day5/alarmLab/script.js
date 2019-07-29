console.log("script is running...");
function myAlarm(wakeup){ 
    console.log("Hey, mariama wake up" + wakeup );
    document.write("hey, mariama wake up its"+ wakeup)
}

myAlarm("6am");

function dadAlarm(wakeup){
    console.log ("hey dad, Its time to wake up");
    document.write("hey, dad its time to wake up");
} 


function importantAlarm(myMessage){
    return myMessage.toUpperCase();
    
}

console.log( importantAlarm("wake up, its time") ); 


function snoozAlarm(Mariama){

    return "The alarm for " + Mariama + " has been changed to " +(Mariama+1);
}

console.log( snoozAlarm(7) );
