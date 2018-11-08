# mqmigrate
Migration tool for WebSphere MQ

## Goal
The article [Evolutionary Database Design](https://www.martinfowler.com/articles/evodb.html) written by Martin Fowler explains why migration tools are important:

> *Over the last decade we've developed and refined a number of techniques that allow a database design to evolve as an application develops. This is a very important capability for agile methodologies. The techniques rely on applying continuous integration and automated refactoring to database development, together with a close collaboration between DBAs and application developers.*

Replace *database* with *WebSphere MQ* and *DBAs* with *MQ administrators* in the introduction of this article and you get the goal of this project. There are a lot of migration tools for managing the schemas of databases (like [Phinx](https://phinx.org) for example). The goal of this project is to create such a tool for managing the objects of WebSphere MQ : define queues, remove queues, define channels, set security, ...

## How?
There are two ways of managing queuemanager objects:

+ MQSC commands
+ PCF commands

### MQSC
MQSC commands are processed by the runmqsc commandline tool of WebSphere MQ. The migration tool must be capable of writing these commands in a file and pass it to runmqsc.

### PCF
PCF commands are actually MQSC commands that are send as a message to the command server of the queuemanager. For this you need a script or a tool that can send PCF messages to a queuemanager. There are MQ bindings ([Python](https://pypi.org/project/pymqi/) for example) that allow scripts to create such messages. Use [MQWeb](https://www.mqweb.org) is another possibility.

Currently this project is in an experimental phase.
