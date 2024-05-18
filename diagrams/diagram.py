# diagram.py
from diagrams import Diagram, Cluster
from diagrams.aws.network import CF
from diagrams.aws.storage import S3
from diagrams.saas.cdn import Cloudflare

with Diagram("fa-cdn", show=False):
    dns = Cloudflare("Cloudflare DNS")

    with Cluster("AWS"):
        aws = CF("Cloudfront CDN")
        aws >> S3("S3 Static Assets")

    dns >> aws