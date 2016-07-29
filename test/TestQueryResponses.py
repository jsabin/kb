environments = [{
    "environment_name": "lab",
    "name": "foo",
    "type": "environment",
    "svc_id": "52",
    "note": "rcollette ops bootcamp"
}, {
    "environment_name": "lab",
    "name": "bar",
    "type": "environment",
    "svc_id": "54",
    "note": "Ben Test Env"
}, {
    "environment_name": "lab",
    "name": "fi",
    "type": "environment",
    "svc_id": "59",
    "note": "My Laaab"
}]

instances = [
    {
        "bios_version" : "Bochs",
        "operating_system" : "CentOS",
        "operating_system_release" : "6.5",
        "kernel_release" : "2.6.32-431.1.2.0.1.el6.x86_64",
        "fqdn" : "m0051672.lab.ppops.net",
        "agent_type" : "factloader/0.7.3",
        "inventory_component_type" : "system",
        "monitoring_status" : "auto",
        "created_by" : "foo",
        "memory_size" : "3.87 GB",
        "size" : "m2.medium",
        "virtual" : "kvm",
        "tags" : "6.5, labproxy - Alerting Server",
        "image" : "centos6.5",
        "netdriver" : "virtio_net",
        "hardware_test_name" : "None",
        "cloud" : "PICLAB_SNV",
        "environment_name" : "jsabin27",
        "config_agent_timestamp" : "2016-07-01 18:50:05",
        "host_fqdn" : "m0076038.ppops.net",
        "status" : "idle",
        "physical_processor_count" : "2",
        "date_created" : "2014-11-07 22:07:35",
        "interfaces" : "eth0,lo",
        "ip_address" : "410.421.445.176",
        "date_modified" : "2016-07-01 21:00:24",
        "svc_id" : "event-indexer",
        "roles" : "event-indexer-aws"
    },
    {
        "bios_version" : "Bochs",
        "operating_system" : "CentOS",
        "operating_system_release" : "5.6",
        "kernel_release" : "2.6.18-238.19.1.el5.centos.plus",
        "fqdn" : "m0053440.lab.ppops.net",
        "agent_type" : "factloader/0.7.3",
        "memory_size" : "1.96 GB",
        "size" : "m1.small",
        "virtual" : "physical",
        "tags" : "collector, test, replayer",
        "image" : "centos5.6",
        "hardware_test_name" : "None",
        "manufacturer" : "Bochs",
        "bios_vendor" : "Bochs",
        "cloud" : "PICLAB_SNV",
        "environment_name" : "jsabin27",
        "config_agent_timestamp" : "2016-07-01 14:39:15",
        "host_fqdn" : "m0006009.ppops.net",
        "status" : "idle",
        "physical_processor_count" : "0",
        "date_created" : "2015-03-04 16:17:46",
        "interfaces" : "eth0,sit0",
        "is_virtual" : "false",
        "ip_address" : "310.221.143.157",
        "date_modified" : "2016-07-01 21:00:30",
        "svc_id" : None,
        "roles" : ""
    }
]

services = [{
    "dmz_cidr": "1.2.3.4/0",
    "backend_gateway": "11.22.47.254",
    "environment_name": "foo",
    "name": "Foo2",
    "network_ip_range": "11.21.43.1/24",
    "openstack_network_host": "21.21.21.21",
    "admin_host": "foo.bar.com",
    "openstack_controller": "110.121.132.175",
    "backend_routing": "true",
    "svc_id": "16",
    "type": "PIC",
    "openstack_api_host": "110.211.312.715"
}, {
    "environment_name": "lab2",
    "version": "1.5.3-3",
    "name": "Foo1",
    "scoring_backend:nodes": "fi.foo.bar:8443",
    "type": "service",
    "svc_id": "4387",
    "port": "443"
}, {
    "environment_name": "foo",
    "name": "fee",
    "svc_id": "1855",
    "type": "service",
}]

properties = {
    "a": "1",
    "b": "2",
    "c": "3",
    "d": "4",
    "e": "5",
    "f": "6",
    "g": "7",
    "h": "8",
}

clouds = ["cloud1", "cloud2", "cloud3"]

sizes = [{"id": "m1.small", "provider_id": "m1.small", "name": "Small Instance", "ram": 1740.8, "disk": 160, "cores": 1, "description": "Small Instance", "price": 32},
         {"id": "m1.medium", "provider_id": "m1.medium", "name": "Medium Instance", "ram": 3750, "disk": 400, "cores": 2, "description": "Medium Instance", "price": 63},
         {"id": "m1.large", "provider_id": "m1.large", "name": "Large Instance", "ram": 7680, "disk": 850, "cores": 4, "description": "Large Instance", "price": 126},
         {"id": "c1.xlarge", "provider_id": "c1.xlarge", "name": "High-CPU Extra Large", "ram": 7168, "disk": 1690, "cores": 20, "description": "High-CPU Extra Large",
          "price": 375}, ]

images = [
    {"id": "centos6.6", "provider_id": "ami-2fc12c44", "name": "c66_v1", "description": "CentOS release 6.6", "ramdisk_id": '', "kernel_id": "aki-919dcaf8", "osfamily": "RedHat",
     "operatingsystem": "CentOS", "operatingsystemrelease": "6.6"},
    {"id": "centos6.6HVM", "provider_id": "ami-050a4e60", "name": "Centos 6.6v1 HVM-EBS", "description": "Centos 6.6v1 HVM-EBS", "ramdisk_id": '', "kernel_id": '',
     "osfamily": "RedHat", "operatingsystem": "CentOS", "operatingsystemrelease": "6.6"},
    {"id": "centos6.5L", "provider_id": "ami-e46f458c", "name": "c65_v5L", "description": "CentOS 6.5 (Legacy)", "ramdisk_id": '', "kernel_id": "aki-919dcaf8",
     "osfamily": "RedHat", "operatingsystem": "CentOS", "operatingsystemrelease": "6.5"},
]
