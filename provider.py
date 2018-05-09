#!/usr/bin/env python
import sys
import boto3


def terminate_instance():
    ec2 = boto3.resource('ec2')
    for instance_id in sys.argv[1:]:
        instance = ec2.Instance(instance_id)
        response = instance.terminate()
        print(response)

def list_instance():
    ec2 = boto3.resource('ec2')
    for instance in ec2.instances.all():
        print(instance.id, instance.state)

def create_instance():
    ec2 = boto3.resource('ec2')
    instance = ec2.create_instances(
        ImageId = 'ami-916f59f4',
        MinCount = 1,
        MaxCount = 1,
        InstanceType = 't2.micro'
    )
    print(instance[0].id)

def instruction():
    print("Welcome to AWS EC2 ---- ")
    print("(a) create instance")
    print("(b) terminate instance")
    print("(c) list all instances")
    print("(q) quit")

def main():
    instruction()
    option = ''
    while (option != 'q'):
        option = input('Please select your option: ')
        if option == 'a':
            create_instance()
        elif option == 'b':
            terminate_instance()
        elif option == 'c':
            list_instance()
    print("Program Exited")


if __name__ == "__main__":
    main()
