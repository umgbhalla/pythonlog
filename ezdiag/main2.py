from os import memfd_create
from diagrams import Cluster, Diagram

from diagrams.aws.compute import EC2, ECS
from diagrams.aws.database import RDS, ElastiCache
from diagrams.aws.network import ELB, Route53

with Diagram("Grouped Workers", show=True):  # direction="TR"
    dns = Route53("dns")
    lb = ELB("lb")
    with Cluster("Service"):
        svg_group = [ECS("web1"), ECS("web2"), ECS("web3")]
    with Cluster("DB cluster"):
        db_master = RDS("userdb")
        db_master - [RDS("userdb_back")]
    memcache = ElastiCache("memcached")
    dns >> lb >> svg_group
    svg_group >> db_master
    svg_group >> memcache
