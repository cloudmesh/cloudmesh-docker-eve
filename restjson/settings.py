
Host = {
    'schema': {
        'Name': {
            'type': 'string'
        },
        'Ip': {
            'type': 'string'
        },
        'Port': {
            'type': 'integer'
        },
        'Swarmmanager': {
            'type': 'boolean'
        }
    }
}

Image = {
    'schema': {
        'Created': {
            'type': 'integer'
        },
        'Labels': {
            'type': 'dict',
            'schema': {}
        },
        'VirtualSize': {
            'type': 'integer'
        },
        'SharedSize': {
            'type': 'integer'
        },
        'ParentId': {
            'type': 'string'
        },
        'Size': {
            'type': 'integer'
        },
        'RepoDigests': {
            'type': 'list',
            'schema': {
                'type': 'string'
            }
        },
        'Id': {
            'type': 'string'
        },
        'Ip': {
            'type': 'string'
        },
        'Containers': {
            'type': 'integer'
        },
        'RepoTags': {
            'type': 'list',
            'schema': {
                'type': 'string'
            }
        }
    }
}

Container = {
    'schema': {
        'ExecIDs': {
            'nullable': True
        },
        'State': {
            'type': 'dict',
            'schema': {
                'Status': {
                    'type': 'string'
                },
                'Pid': {
                    'type': 'integer'
                },
                'OOMKilled': {
                    'type': 'boolean'
                },
                'Dead': {
                    'type': 'boolean'
                },
                'Paused': {
                    'type': 'boolean'
                },
                'Running': {
                    'type': 'boolean'
                },
                'FinishedAt': {
                    'type': 'string'
                },
                'Restarting': {
                    'type': 'boolean'
                },
                'Error': {
                    'type': 'string'
                },
                'StartedAt': {
                    'type': 'string'
                },
                'ExitCode': {
                    'type': 'integer'
                }
            }
        },
        'Config': {
            'type': 'dict',
            'schema': {
                'Tty': {
                    'type': 'boolean'
                },
                'Cmd': {
                    'type': 'list',
                    'schema': {
                        'type': 'string'
                    }
                },
                'Volumes': {
                    'nullable': True
                },
                'Domainname': {
                    'type': 'string'
                },
                'WorkingDir': {
                    'type': 'string'
                },
                'Image': {
                    'type': 'string'
                },
                'Hostname': {
                    'type': 'string'
                },
                'StdinOnce': {
                    'type': 'boolean'
                },
                'Labels': {
                    'type': 'dict',
                    'schema': {}
                },
                'AttachStdin': {
                    'type': 'boolean'
                },
                'User': {
                    'type': 'string'
                },
                'Env': {
                    'type': 'list',
                    'schema': {
                        'type': 'string'
                    }
                },
                'Entrypoint': {
                    'nullable': True
                },
                'OnBuild': {
                    'nullable': True
                },
                'AttachStderr': {
                    'type': 'boolean'
                },
                'AttachStdout': {
                    'type': 'boolean'
                },
                'OpenStdin': {
                    'type': 'boolean'
                }
            }
        },
        'ResolvConfPath': {
            'type': 'string'
        },
        'HostsPath': {
            'type': 'string'
        },
        'Args': {
            'type': 'list',
            'schema': {}
        },
        'Driver': {
            'type': 'string'
        },
        'Path': {
            'type': 'string'
        },
        'HostnamePath': {
            'type': 'string'
        },
        'RestartCount': {
            'type': 'integer'
        },
        'Name': {
            'type': 'string'
        },
        'Created': {
            'type': 'string'
        },
        'GraphDriver': {
            'type': 'dict',
            'schema': {
                'Data': {
                    'type': 'dict',
                    'schema': {
                        'MergedDir': {
                            'type': 'string'
                        },
                        'WorkDir': {
                            'type': 'string'
                        },
                        'LowerDir': {
                            'type': 'string'
                        },
                        'UpperDir': {
                            'type': 'string'
                        }
                    }
                },
                'Name': {
                    'type': 'string'
                }
            }
        },
        'Mounts': {
            'type': 'list',
            'schema': {}
        },
        'ProcessLabel': {
            'type': 'string'
        },
        'NetworkSettings': {
            'type': 'dict',
            'schema': {
                'Bridge': {
                    'type': 'string'
                },
                'Networks': {
                    'type': 'dict',
                    'schema': {
                        'bridge': {
                            'type': 'dict',
                            'schema': {
                                'NetworkID': {
                                    'type': 'string'
                                },
                                'MacAddress': {
                                    'type': 'string'
                                },
                                'GlobalIPv6PrefixLen': {
                                    'type': 'integer'
                                },
                                'Links': {
                                    'nullable': True
                                },
                                'GlobalIPv6Address': {
                                    'type': 'string'
                                },
                                'IPv6Gateway': {
                                    'type': 'string'
                                },
                                'IPAMConfig': {
                                    'nullable': True
                                },
                                'EndpointID': {
                                    'type': 'string'
                                },
                                'IPPrefixLen': {
                                    'type': 'integer'
                                },
                                'IPAddress': {
                                    'type': 'string'
                                },
                                'Gateway': {
                                    'type': 'string'
                                },
                                'Aliases': {
                                    'nullable': True
                                }
                            }
                        }
                    }
                },
                'SecondaryIPv6Addresses': {
                    'nullable': True
                },
                'LinkLocalIPv6Address': {
                    'type': 'string'
                },
                'HairpinMode': {
                    'type': 'boolean'
                },
                'IPv6Gateway': {
                    'type': 'string'
                },
                'SecondaryIPAddresses': {
                    'nullable': True
                },
                'SandboxID': {
                    'type': 'string'
                },
                'MacAddress': {
                    'type': 'string'
                },
                'GlobalIPv6Address': {
                    'type': 'string'
                },
                'Gateway': {
                    'type': 'string'
                },
                'LinkLocalIPv6PrefixLen': {
                    'type': 'integer'
                },
                'EndpointID': {
                    'type': 'string'
                },
                'SandboxKey': {
                    'type': 'string'
                },
                'GlobalIPv6PrefixLen': {
                    'type': 'integer'
                },
                'IPPrefixLen': {
                    'type': 'integer'
                },
                'IPAddress': {
                    'type': 'string'
                },
                'Ports': {
                    'nullable': True
                }
            }
        },
        'AppArmorProfile': {
            'type': 'string'
        },
        'Image': {
            'type': 'string'
        },
        'LogPath': {
            'type': 'string'
        },
        'HostConfig': {
            'type': 'dict',
            'schema': {
                'CpuPeriod': {
                    'type': 'integer'
                },
                'MemorySwappiness': {
                    'type': 'integer'
                },
                'ContainerIDFile': {
                    'type': 'string'
                },
                'KernelMemory': {
                    'type': 'integer'
                },
                'Memory': {
                    'type': 'integer'
                },
                'CpuQuota': {
                    'type': 'integer'
                },
                'UsernsMode': {
                    'type': 'string'
                },
                'AutoRemove': {
                    'type': 'boolean'
                },
                'BlkioDeviceReadIOps': {
                    'nullable': True
                },
                'Dns': {
                    'type': 'list',
                    'schema': {}
                },
                'ExtraHosts': {
                    'nullable': True
                },
                'PidsLimit': {
                    'type': 'integer'
                },
                'DnsSearch': {
                    'type': 'list',
                    'schema': {}
                },
                'Privileged': {
                    'type': 'boolean'
                },
                'IOMaximumIOps': {
                    'type': 'integer'
                },
                'CpuPercent': {
                    'type': 'integer'
                },
                'NanoCpus': {
                    'type': 'integer'
                },
                'Ulimits': {
                    'nullable': True
                },
                'CpusetCpus': {
                    'type': 'string'
                },
                'DiskQuota': {
                    'type': 'integer'
                },
                'CgroupParent': {
                    'type': 'string'
                },
                'BlkioWeight': {
                    'type': 'integer'
                },
                'RestartPolicy': {
                    'type': 'dict',
                    'schema': {
                        'MaximumRetryCount': {
                            'type': 'integer'
                        },
                        'Name': {
                            'type': 'string'
                        }
                    }
                },
                'OomScoreAdj': {
                    'type': 'integer'
                },
                'BlkioDeviceReadBps': {
                    'nullable': True
                },
                'VolumeDriver': {
                    'type': 'string'
                },
                'ReadonlyRootfs': {
                    'type': 'boolean'
                },
                'CpuShares': {
                    'type': 'integer'
                },
                'PublishAllPorts': {
                    'type': 'boolean'
                },
                'MemoryReservation': {
                    'type': 'integer'
                },
                'BlkioWeightDevice': {
                    'nullable': True
                },
                'ConsoleSize': {
                    'type': 'list',
                    'schema': {
                        'type': 'integer'
                    }
                },
                'NetworkMode': {
                    'type': 'string'
                },
                'BlkioDeviceWriteBps': {
                    'nullable': True
                },
                'Isolation': {
                    'type': 'string'
                },
                'GroupAdd': {
                    'nullable': True
                },
                'CpuRealtimeRuntime': {
                    'type': 'integer'
                },
                'Devices': {
                    'type': 'list',
                    'schema': {}
                },
                'BlkioDeviceWriteIOps': {
                    'nullable': True
                },
                'Binds': {
                    'nullable': True
                },
                'CpusetMems': {
                    'type': 'string'
                },
                'Cgroup': {
                    'type': 'string'
                },
                'UTSMode': {
                    'type': 'string'
                },
                'PidMode': {
                    'type': 'string'
                },
                'Runtime': {
                    'type': 'string'
                },
                'VolumesFrom': {
                    'nullable': True
                },
                'CapDrop': {
                    'nullable': True
                },
                'DnsOptions': {
                    'type': 'list',
                    'schema': {}
                },
                'ShmSize': {
                    'type': 'integer'
                },
                'Links': {
                    'nullable': True
                },
                'CpuRealtimePeriod': {
                    'type': 'integer'
                },
                'IpcMode': {
                    'type': 'string'
                },
                'PortBindings': {
                    'type': 'dict',
                    'schema': {}
                },
                'SecurityOpt': {
                    'nullable': True
                },
                'CapAdd': {
                    'nullable': True
                },
                'CpuCount': {
                    'type': 'integer'
                },
                'MemorySwap': {
                    'type': 'integer'
                },
                'OomKillDisable': {
                    'type': 'boolean'
                },
                'LogConfig': {
                    'type': 'dict',
                    'schema': {
                        'Config': {
                            'type': 'dict',
                            'schema': {}
                        },
                        'Type': {
                            'type': 'string'
                        }
                    }
                },
                'IOMaximumBandwidth': {
                    'type': 'integer'
                }
            }
        },
        'Id': {
            'type': 'string'
        },
        'Ip': {
            'type': 'string'
        },
        'MountLabel': {
            'type': 'string'
        }
    }
}

Network = {
    'schema': {
        'Options': {
            'type': 'dict',
            'schema': {
                'com.docker.network.bridge.name': {
                    'type': 'string'
                },
                'com.docker.network.bridge.default_bridge': {
                    'type': 'string'
                },
                'com.docker.network.bridge.enable_ip_masquerade': {
                    'type': 'string'
                },
                'com.docker.network.driver.mtu': {
                    'type': 'string'
                },
                'com.docker.network.bridge.host_binding_ipv4': {
                    'type': 'string'
                },
                'com.docker.network.bridge.enable_icc': {
                    'type': 'string'
                }
            }
        },
        'Name': {
            'type': 'string'
        },
        'Created': {
            'type': 'string'
        },
        'EnableIPv6': {
            'type': 'boolean'
        },
        'Labels': {
            'type': 'dict',
            'schema': {}
        },
        'Driver': {
            'type': 'string'
        },
        'Attachable': {
            'type': 'boolean'
        },
        'Internal': {
            'type': 'boolean'
        },
        'IPAM': {
            'type': 'dict',
            'schema': {
                'Config': {
                    'type': 'list',
                    'schema': {
                        'type': 'dict',
                        'schema': {
                            'Subnet': {
                                'type': 'string'
                            },
                            'Gateway': {
                                'type': 'string'
                            }
                        }
                    }
                },
                'Driver': {
                    'type': 'string'
                },
                'Options': {
                    'nullable': True
                }
            }
        },
        'Scope': {
            'type': 'string'
        },
        'Id': {
            'type': 'string'
        },
        'Ip': {
            'type': 'string'
        },
        'Containers': {
            'type': 'dict',
            'schema': {}
        }
    }
}

Service = {
    'schema': {
        'Endpoint': {
            'type': 'dict',
            'schema': {
                'VirtualIPs': {
                    'type': 'list',
                    'schema': {
                        'type': 'dict',
                        'schema': {
                            'NetworkID': {
                                'type': 'string'
                            },
                            'Addr': {
                                'type': 'string'
                            }
                        }
                    }
                },
                'Spec': {
                    'type': 'dict',
                    'schema': {
                        'Mode': {
                            'type': 'string'
                        },
                        'Ports': {
                            'type': 'list',
                            'schema': {
                                'type': 'dict',
                                'schema': {
                                    'TargetPort': {
                                        'type': 'integer'
                                    },
                                    'PublishedPort': {
                                        'type': 'integer'
                                    },
                                    'Protocol': {
                                        'type': 'string'
                                    },
                                    'PublishMode': {
                                        'type': 'string'
                                    }
                                }
                            }
                        }
                    }
                },
                'Ports': {
                    'type': 'list',
                    'schema': {
                        'type': 'dict',
                        'schema': {
                            'TargetPort': {
                                'type': 'integer'
                            },
                            'PublishedPort': {
                                'type': 'integer'
                            },
                            'Protocol': {
                                'type': 'string'
                            },
                            'PublishMode': {
                                'type': 'string'
                            }
                        }
                    }
                }
            }
        },
        'ID': {
            'type': 'string'
        },
        'Ip': {
            'type': 'string'
        },
        'Version': {
            'type': 'dict',
            'schema': {
                'Index': {
                    'type': 'integer'
                }
            }
        },
        'PreviousSpec': {
            'type': 'dict',
            'schema': {
                'Name': {
                    'type': 'string'
                },
                'EndpointSpec': {
                    'type': 'dict',
                    'schema': {
                        'Mode': {
                            'type': 'string'
                        },
                        'Ports': {
                            'type': 'list',
                            'schema': {
                                'type': 'dict',
                                'schema': {
                                    'TargetPort': {
                                        'type': 'integer'
                                    },
                                    'PublishedPort': {
                                        'type': 'integer'
                                    },
                                    'Protocol': {
                                        'type': 'string'
                                    },
                                    'PublishMode': {
                                        'type': 'string'
                                    }
                                }
                            }
                        }
                    }
                },
                'UpdateConfig': {
                    'type': 'dict',
                    'schema': {
                        'MaxFailureRatio': {
                            'type': 'integer'
                        },
                        'Parallelism': {
                            'type': 'integer'
                        },
                        'FailureAction': {
                            'type': 'string'
                        }
                    }
                },
                'Mode': {
                    'type': 'dict',
                    'schema': {
                        'Replicated': {
                            'type': 'dict',
                            'schema': {
                                'Replicas': {
                                    'type': 'integer'
                                }
                            }
                        }
                    }
                },
                'Networks': {
                    'type': 'list',
                    'schema': {
                        'type': 'dict',
                        'schema': {
                            'Target': {
                                'type': 'string'
                            }
                        }
                    }
                },
                'TaskTemplate': {
                    'type': 'dict',
                    'schema': {
                        'Placement': {
                            'type': 'dict',
                            'schema': {}
                        },
                        'ContainerSpec': {
                            'type': 'dict',
                            'schema': {
                                'Image': {
                                    'type': 'string'
                                },
                                'DNSConfig': {
                                    'type': 'dict',
                                    'schema': {}
                                },
                                'Env': {
                                    'type': 'list',
                                    'schema': {
                                        'type': 'string'
                                    }
                                }
                            }
                        },
                        'Networks': {
                            'type': 'list',
                            'schema': {
                                'type': 'dict',
                                'schema': {
                                    'Target': {
                                        'type': 'string'
                                    }
                                }
                            }
                        },
                        'RestartPolicy': {
                            'type': 'dict',
                            'schema': {
                                'MaxAttempts': {
                                    'type': 'integer'
                                },
                                'Condition': {
                                    'type': 'string'
                                }
                            }
                        },
                        'ForceUpdate': {
                            'type': 'integer'
                        },
                        'Resources': {
                            'type': 'dict',
                            'schema': {
                                'Reservations': {
                                    'type': 'dict',
                                    'schema': {}
                                },
                                'Limits': {
                                    'type': 'dict',
                                    'schema': {}
                                }
                            }
                        }
                    }
                }
            }
        },
        'UpdatedAt': {
            'type': 'string'
        },
        'UpdateStatus': {
            'type': 'dict',
            'schema': {
                'StartedAt': {
                    'type': 'string'
                },
                'CompletedAt': {
                    'type': 'string'
                }
            }
        },
        'Spec': {
            'type': 'dict',
            'schema': {
                'Name': {
                    'type': 'string'
                },
                'EndpointSpec': {
                    'type': 'dict',
                    'schema': {
                        'Mode': {
                            'type': 'string'
                        },
                        'Ports': {
                            'type': 'list',
                            'schema': {
                                'type': 'dict',
                                'schema': {
                                    'TargetPort': {
                                        'type': 'integer'
                                    },
                                    'PublishedPort': {
                                        'type': 'integer'
                                    },
                                    'Protocol': {
                                        'type': 'string'
                                    },
                                    'PublishMode': {
                                        'type': 'string'
                                    }
                                }
                            }
                        }
                    }
                },
                'UpdateConfig': {
                    'type': 'dict',
                    'schema': {
                        'MaxFailureRatio': {
                            'type': 'integer'
                        },
                        'Parallelism': {
                            'type': 'integer'
                        },
                        'FailureAction': {
                            'type': 'string'
                        }
                    }
                },
                'Mode': {
                    'type': 'dict',
                    'schema': {
                        'Replicated': {
                            'type': 'dict',
                            'schema': {
                                'Replicas': {
                                    'type': 'integer'
                                }
                            }
                        }
                    }
                },
                'Networks': {
                    'type': 'list',
                    'schema': {
                        'type': 'dict',
                        'schema': {
                            'Target': {
                                'type': 'string'
                            }
                        }
                    }
                },
                'TaskTemplate': {
                    'type': 'dict',
                    'schema': {
                        'Placement': {
                            'type': 'dict',
                            'schema': {}
                        },
                        'ContainerSpec': {
                            'type': 'dict',
                            'schema': {
                                'Image': {
                                    'type': 'string'
                                },
                                'DNSConfig': {
                                    'type': 'dict',
                                    'schema': {}
                                },
                                'Env': {
                                    'type': 'list',
                                    'schema': {
                                        'type': 'string'
                                    }
                                }
                            }
                        },
                        'Networks': {
                            'type': 'list',
                            'schema': {
                                'type': 'dict',
                                'schema': {
                                    'Target': {
                                        'type': 'string'
                                    }
                                }
                            }
                        },
                        'RestartPolicy': {
                            'type': 'dict',
                            'schema': {
                                'MaxAttempts': {
                                    'type': 'integer'
                                },
                                'Condition': {
                                    'type': 'string'
                                }
                            }
                        },
                        'ForceUpdate': {
                            'type': 'integer'
                        },
                        'Resources': {
                            'type': 'dict',
                            'schema': {
                                'Reservations': {
                                    'type': 'dict',
                                    'schema': {}
                                },
                                'Limits': {
                                    'type': 'dict',
                                    'schema': {}
                                }
                            }
                        }
                    }
                }
            }
        },
        'CreatedAt': {
            'type': 'string'
        }
    }
}

Node = {
    'schema': {
        'Status': {
            'type': 'dict',
            'schema': {
                'State': {
                    'type': 'string'
                },
                'Addr': {
                    'type': 'string'
                }
            }
        },
        'Description': {
            'type': 'dict',
            'schema': {
                'Engine': {
                    'type': 'dict',
                    'schema': {
                        'Plugins': {
                            'type': 'list',
                            'schema': {
                                'type': 'dict',
                                'schema': {
                                    'Type': {
                                        'type': 'string'
                                    },
                                    'Name': {
                                        'type': 'string'
                                    }
                                }
                            }
                        },
                        'EngineVersion': {
                            'type': 'string'
                        }
                    }
                },
                'Platform': {
                    'type': 'dict',
                    'schema': {
                        'OS': {
                            'type': 'string'
                        },
                        'Architecture': {
                            'type': 'string'
                        }
                    }
                },
                'Hostname': {
                    'type': 'string'
                },
                'Resources': {
                    'type': 'dict',
                    'schema': {
                        'MemoryBytes': {
                            'type': 'integer'
                        },
                        'NanoCPUs': {
                            'type': 'integer'
                        }
                    }
                }
            }
        },
        'ID': {
            'type': 'string'
        },
        'Ip': {
            'type': 'string'
        },
        'Version': {
            'type': 'dict',
            'schema': {
                'Index': {
                    'type': 'integer'
                }
            }
        },
        'ManagerStatus': {
            'type': 'dict',
            'schema': {
                'Reachability': {
                    'type': 'string'
                },
                'Leader': {
                    'type': 'boolean'
                },
                'Addr': {
                    'type': 'string'
                }
            }
        },
        'UpdatedAt': {
            'type': 'string'
        },
        'Spec': {
            'type': 'dict',
            'schema': {
                'Role': {
                    'type': 'string'
                },
                'Availability': {
                    'type': 'string'
                }
            }
        },
        'CreatedAt': {
            'type': 'string'
        }
    }
}



eve_settings = {
    'MONGO_HOST': 'localhost',
    'MONGO_DBNAME': 'testing',
    'RESOURCE_METHODS': ['GET', 'POST', 'DELETE'],
    'ITEM_METHODS' : ['GET','PATCH','PUT','DELETE'],
    'BANDWIDTH_SAVER': False,
    'MONGO_QUERY_BLACKLIST' : ['$regex'],
    'DOMAIN': {
        'Host': Host,
        'Image': Image,
        'Container': Container,
        'Network': Network,
        'Service': Service,
        'Node': Node,
    },
}
