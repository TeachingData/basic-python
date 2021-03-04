import sqlite3
import sys
import datetime

conn = sqlite3.connect('Events.db')
c = conn.cursor()

## Get last attendance id (dynamic remember) #technically do this last
c.execute("select attendance_id from attending order by attendance_id desc limit 1;")
attend_id = int(c.fetchone()[0]) + 1

## Get user id
user_id = int(input("What's your competitor number?")) ## add try here

# use a prepared statement for your selects (execute and commit our single statement)
### Here "?" is our placeholder & to pass user_id we put it in a set
c.execute("SELECT comp_name FROM competitors WHERE comp_id=?;", (user_id,))

# use fetchone to only get a single value
### (it still returns a set so we only need the actual first value)
user_name = c.fetchone()[0]
if (not user_name):
    ## I'm just going to exit if you cannot even give me a good id (no loop here)
    print("That's not a value id.")
    sys.exit()
# don't need else cause if we are here we didn't exit (so user_id is valid)
print(f"Welcome {user_name}!")

## So now let's get the possible (dynamic) events from today (then today + 5)
#print(f"today is {datetime.date.today().month}/{datetime.date.today().day}")

# Build a Month variable (from datetime)
month = str(datetime.date.today().month) + "%"
day = str(datetime.date.today().day + 5).zfill(2)

events = []
for row in c.execute("select event_id, event_descript, event_date from events where event_date like ?;",
    #(str(datetime.date.today().month) + '%',)):
    (month.zfill(3),)): # zfill is "zero fill - so make 3 characters by adding 0s to front"
        if (row[2][3:5] >= day): # use a string slice to find if day is 5 days away
            print(f"Available events include {row[0]} : {row[1]} on {row[2]}\n")
            
            # Now let's see if this person is attending and then add it to our list of events if yes
            attend = input("Will you attend this event? (y/n)")
            if attend.lower().startswith('y'):
                attend_id = attend_id + 1
                events.append((attend_id, row[0], user_id))

insert = "INSERT INTO attending(attendance_id,event_id,comp_id) VALUES ("
### Okay, technically you can just add 3 ? (we will always have 3) but to show a dynamic method:

#for i in events: # build our insert string (add ? for each & then slice it)
#    insert = insert + "?,"
#insert = insert[:-1] + ");"

#### or better: I love you join & string repeat
insert += ", ".join("?" * len(events)) + ");"

print(insert)
print(events)

c.executemany(insert, events)

## commit - cause this whole thing is wrapped in a BEGIN TRANSACTION (leave out commit and nothing seems to happen)
#### it rollsback automatically
conn.commit()
conn.close()
