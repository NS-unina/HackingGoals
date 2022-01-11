from typedb.client import *

with TypeDB.core_client('localhost:1729') as client: 
    with client.session("hacking_goal", SessionType.DATA) as session:
        print("Session")
        print(session)
        with session.transaction(TransactionType.READ) as tx:
            id_target_task = 5
            temp_task = id_target_task
            end = False
            while not end:
                query = [
                    'match',
                    '	$t1 isa h-task, has h-id %d;' % id_target_task,
                    '	$t2 isa h-task, has h-id $h-id;',
                    '	$r(master: $t2, dependant: $t1) isa master-to-dependant;',
                    '	get $h-id;'
                ]
                print ("\nQuery:\n", "\n".join(query))
                query = "".join(query)
                iterator = tx.query().match(query)
                answers = [ ans.get("h-id") for ans in iterator ]
                if answers:
                    result = [answer.value() for answer in answers]
                    temp_task = id_target_task
                    id_target_task = result[0]
                else:
                    end = True
            if temp_task != id_target_task:
                query = [
                    'match',
                    '	$t1 isa h-task, has h-id %d;' % id_target_task,
                    '	$at1 isa h-attack, has h-id $h-id;',
                    '	$r isa resource;',
                    '	$rel1(is-made-by: $t1, makes: $at1) isa task-to-attack;',
                    '	$rel2(acquires: $at1, is-acquired: $r) isa acquired-knowledge;',
                    '	$t2 isa h-task, has h-id %d;' % temp_task,
                    '	$rel3(requires: $t2, is-required: $r) isa required-knowledge;',
                    '	get $h-id;'
                ]
                print ("\nQuery:\n", "\n".join(query))
                query = "".join(query)
                iterator = tx.query(query)
                new_answers = [ ans.get("h-id") for ans in iterator ]
                if new_answers:
                    result = [answer.value() for answer in new_answers]
                    print("\nTask %d executable\n" % id_target_task)
                    print("Attack to execute: %d\n" % result[0])
                else:
                    print("\nCan't determine which attack to execute of task %d\n" % id_target_task)
            else:
                print("\nNo attacks available, task %d is executable\n" % id_target_task)
            pass
        pass
