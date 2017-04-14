
Host = {
    'allow_unknown': True,
    'schema': {
        'Name': {
            'type': 'string',
            'nullable': True
        },
        'Ip': {
            'type': 'string',
            'nullable': True
        },
        'Port': {
            'type': 'integer',
            'nullable': True
        },
        'Swarmmanager': {
            'type': 'boolean',
            'nullable': True
        }
    }
}

Image = {
    'allow_unknown': True,
    'schema': {
        'Created': {
            'type': 'integer',
            'nullable': True
        },
        'Labels': {
            'type': 'dict',
            'nullable': True,
            'schema': {}
        },
        'VirtualSize': {
            'type': 'integer',
            'nullable': True
        },
        'SharedSize': {
            'type': 'integer',
            'nullable': True
        },
        'ParentId': {
            'type': 'string',
            'nullable': True
        },
        'Size': {
            'type': 'integer',
            'nullable': True
        },
        'RepoDigests': {
            'type': 'list',
            'nullable': True,
            'schema': {
                'type': 'string',
                'nullable': True
            }
        },
        'Id': {
            'type': 'string'
        },
        'Ip': {
            'type': 'string'
        },
        'Containers': {
            'type': 'integer',
            'nullable': True
        },
        'RepoTags': {
            'type': 'list',
            'nullable': True,
            'schema': {
                'type': 'string',
                'nullable': True
            }
        }
    }
}

Container = {
    'allow_unknown': True,
    'schema': {
        'ExecIDs': {
            'nullable': True
        },
        'State': {
            'type': 'dict',
            'nullable': True,
            'schema': {
                'Status': {
                    'type': 'string',
                    'nullable': True
                },
                'Pid': {
                    'type': 'integer',
                    'nullable': True
                },
                'OOMKilled': {
                    'type': 'boolean',
                    'nullable': True
                },
                'Dead': {
                    'type': 'boolean',
                    'nullable': True
                },
                'Paused': {
                    'type': 'boolean',
                    'nullable': True
                },
                'Running': {
                    'type': 'boolean',
                    'nullable': True
                },
                'FinishedAt': {
                    'type': 'string',
                    'nullable': True
                },
                'Restarting': {
                    'type': 'boolean',
                    'nullable': True
                },
                'Error': {
                    'type': 'string',
                    'nullable': True
                },
                'StartedAt': {
                    'type': 'string',
                    'nullable': True
                },
                'ExitCode': {
                    'type': 'integer',
                    'nullable': True
                }
            }
        },
        'Config': {
            'type': 'dict',
            'nullable': True,
            'schema': {
                'Tty': {
                    'type': 'boolean',
                    'nullable': True
                },
                'Cmd': {
                    'type': 'list',
                    'nullable': True,
                    'schema': {
                        'type': 'string',
                        'nullable': True
                    }
                },
                'Volumes': {
                    'nullable': True
                },
                'Domainname': {
                    'type': 'string',
                    'nullable': True
                },
                'WorkingDir': {
                    'type': 'string',
                    'nullable': True
                },
                'Image': {
                    'type': 'string',
                    'nullable': True
                },
                'Hostname': {
                    'type': 'string',
                    'nullable': True
                },
                'StdinOnce': {
                    'type': 'boolean',
                    'nullable': True
                },
                'Labels': {
                    'type': 'dict',
                    'nullable': True,
                    'schema': {}
                },
                'AttachStdin': {
                    'type': 'boolean',
                    'nullable': True
                },
                'User': {
                    'type': 'string',
                    'nullable': True
                },
                'Env': {
                    'type': 'list',
                    'nullable': True,
                    'schema': {
                        'type': 'string',
                        'nullable': True
                    }
                },
                'Entrypoint': {
                    'nullable': True
                },
                'OnBuild': {
                    'nullable': True
                },
                'AttachStderr': {
                    'type': 'boolean',
                    'nullable': True
                },
                'AttachStdout': {
                    'type': 'boolean',
                    'nullable': True
                },
                'OpenStdin': {
                    'type': 'boolean',
                    'nullable': True
                }
            }
        },
        'ResolvConfPath': {
            'type': 'string',
            'nullable': True
        },
        'HostsPath': {
            'type': 'string',
            'nullable': True
        },
        'Args': {
            'type': 'list',
            'nullable': True,
            'schema': {}
        },
        'Driver': {
            'type': 'string',
            'nullable': True
        },
        'Path': {
            'type': 'string',
            'nullable': True
        },
        'HostnamePath': {
            'type': 'string',
            'nullable': True
        },
        'RestartCount': {
            'type': 'integer',
            'nullable': True
        },
        'Name': {
            'type': 'string',
            'nullable': True
        },
        'Created': {
            'type': 'string',
            'nullable': True
        },
        'GraphDriver': {
            'type': 'dict',
            'nullable': True,
            'schema': {
                'Data': {
                    'type': 'dict',
                    'nullable': True,
                    'schema': {
                        'MergedDir': {
                            'type': 'string',
                            'nullable': True
                        },
                        'WorkDir': {
                            'type': 'string',
                            'nullable': True
                        },
                        'LowerDir': {
                            'type': 'string',
                            'nullable': True
                        },
                        'UpperDir': {
                            'type': 'string',
                            'nullable': True
                        }
                    }
                },
                'Name': {
                    'type': 'string',
                    'nullable': True
                }
            }
        },
        'Mounts': {
            'type': 'list',
            'nullable': True,
            'schema': {}
        },
        'ProcessLabel': {
            'type': 'string',
            'nullable': True
        },
        'NetworkSettings': {
            'type': 'dict',
            'nullable': True,
            'schema': {
                'Bridge': {
                    'type': 'string',
                    'nullable': True
                },
                'Networks': {
                    'type': 'dict',
                    'nullable': True,
                    'schema': {
                        'bridge': {
                            'type': 'dict',
                            'nullable': True,
                            'schema': {
                                'NetworkID': {
                                    'type': 'string',
                                    'nullable': True
                                },
                                'MacAddress': {
                                    'type': 'string',
                                    'nullable': True
                                },
                                'GlobalIPv6PrefixLen': {
                                    'type': 'integer',
                                    'nullable': True
                                },
                                'Links': {
                                    'nullable': True
                                },
                                'GlobalIPv6Address': {
                                    'type': 'string',
                                    'nullable': True
                                },
                                'IPv6Gateway': {
                                    'type': 'string',
                                    'nullable': True
                                },
                                'IPAMConfig': {
                                    'nullable': True
                                },
                                'EndpointID': {
                                    'type': 'string',
                                    'nullable': True
                                },
                                'IPPrefixLen': {
                                    'type': 'integer',
                                    'nullable': True
                                },
                                'IPAddress': {
                                    'type': 'string',
                                    'nullable': True
                                },
                                'Gateway': {
                                    'type': 'string',
                                    'nullable': True
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
                    'type': 'string',
                    'nullable': True
                },
                'HairpinMode': {
                    'type': 'boolean',
                    'nullable': True
                },
                'IPv6Gateway': {
                    'type': 'string',
                    'nullable': True
                },
                'SecondaryIPAddresses': {
                    'nullable': True
                },
                'SandboxID': {
                    'type': 'string',
                    'nullable': True
                },
                'MacAddress': {
                    'type': 'string',
                    'nullable': True
                },
                'GlobalIPv6Address': {
                    'type': 'string',
                    'nullable': True
                },
                'Gateway': {
                    'type': 'string',
                    'nullable': True
                },
                'LinkLocalIPv6PrefixLen': {
                    'type': 'integer',
                    'nullable': True
                },
                'EndpointID': {
                    'type': 'string',
                    'nullable': True
                },
                'SandboxKey': {
                    'type': 'string',
                    'nullable': True
                },
                'GlobalIPv6PrefixLen': {
                    'type': 'integer',
                    'nullable': True
                },
                'IPPrefixLen': {
                    'type': 'integer',
                    'nullable': True
                },
                'IPAddress': {
                    'type': 'string',
                    'nullable': True
                },
                'Ports': {
                    'nullable': True
                }
            }
        },
        'AppArmorProfile': {
            'type': 'string',
            'nullable': True
        },
        'Image': {
            'type': 'string',
            'nullable': True
        },
        'LogPath': {
            'type': 'string',
            'nullable': True
        },
        'HostConfig': {
            'type': 'dict',
            'nullable': True,
            'schema': {
                'CpuPeriod': {
                    'type': 'integer',
                    'nullable': True
                },
                'MemorySwappiness': {
                    'type': 'integer',
                    'nullable': True
                },
                'ContainerIDFile': {
                    'type': 'string',
                    'nullable': True
                },
                'KernelMemory': {
                    'type': 'integer',
                    'nullable': True
                },
                'Memory': {
                    'type': 'integer',
                    'nullable': True
                },
                'CpuQuota': {
                    'type': 'integer',
                    'nullable': True
                },
                'UsernsMode': {
                    'type': 'string',
                    'nullable': True
                },
                'AutoRemove': {
                    'type': 'boolean',
                    'nullable': True
                },
                'BlkioDeviceReadIOps': {
                    'nullable': True
                },
                'Dns': {
                    'type': 'list',
                    'nullable': True,
                    'schema': {}
                },
                'ExtraHosts': {
                    'nullable': True
                },
                'PidsLimit': {
                    'type': 'integer',
                    'nullable': True
                },
                'DnsSearch': {
                    'type': 'list',
                    'nullable': True,
                    'schema': {}
                },
                'Privileged': {
                    'type': 'boolean',
                    'nullable': True
                },
                'IOMaximumIOps': {
                    'type': 'integer',
                    'nullable': True
                },
                'CpuPercent': {
                    'type': 'integer',
                    'nullable': True
                },
                'NanoCpus': {
                    'type': 'integer',
                    'nullable': True
                },
                'Ulimits': {
                    'nullable': True
                },
                'CpusetCpus': {
                    'type': 'string',
                    'nullable': True
                },
                'DiskQuota': {
                    'type': 'integer',
                    'nullable': True
                },
                'CgroupParent': {
                    'type': 'string',
                    'nullable': True
                },
                'BlkioWeight': {
                    'type': 'integer',
                    'nullable': True
                },
                'RestartPolicy': {
                    'type': 'dict',
                    'nullable': True,
                    'schema': {
                        'MaximumRetryCount': {
                            'type': 'integer',
                            'nullable': True
                        },
                        'Name': {
                            'type': 'string',
                            'nullable': True
                        }
                    }
                },
                'OomScoreAdj': {
                    'type': 'integer',
                    'nullable': True
                },
                'BlkioDeviceReadBps': {
                    'nullable': True
                },
                'VolumeDriver': {
                    'type': 'string',
                    'nullable': True
                },
                'ReadonlyRootfs': {
                    'type': 'boolean',
                    'nullable': True
                },
                'CpuShares': {
                    'type': 'integer',
                    'nullable': True
                },
                'PublishAllPorts': {
                    'type': 'boolean',
                    'nullable': True
                },
                'MemoryReservation': {
                    'type': 'integer',
                    'nullable': True
                },
                'BlkioWeightDevice': {
                    'nullable': True
                },
                'ConsoleSize': {
                    'type': 'list',
                    'nullable': True,
                    'schema': {
                        'type': 'integer',
                        'nullable': True
                    }
                },
                'NetworkMode': {
                    'type': 'string',
                    'nullable': True
                },
                'BlkioDeviceWriteBps': {
                    'nullable': True
                },
                'Isolation': {
                    'type': 'string',
                    'nullable': True
                },
                'GroupAdd': {
                    'nullable': True
                },
                'CpuRealtimeRuntime': {
                    'type': 'integer',
                    'nullable': True
                },
                'Devices': {
                    'type': 'list',
                    'nullable': True,
                    'schema': {}
                },
                'BlkioDeviceWriteIOps': {
                    'nullable': True
                },
                'Binds': {
                    'nullable': True
                },
                'CpusetMems': {
                    'type': 'string',
                    'nullable': True
                },
                'Cgroup': {
                    'type': 'string',
                    'nullable': True
                },
                'UTSMode': {
                    'type': 'string',
                    'nullable': True
                },
                'PidMode': {
                    'type': 'string',
                    'nullable': True
                },
                'Runtime': {
                    'type': 'string',
                    'nullable': True
                },
                'VolumesFrom': {
                    'nullable': True
                },
                'CapDrop': {
                    'nullable': True
                },
                'DnsOptions': {
                    'type': 'list',
                    'nullable': True,
                    'schema': {}
                },
                'ShmSize': {
                    'type': 'integer',
                    'nullable': True
                },
                'Links': {
                    'nullable': True
                },
                'CpuRealtimePeriod': {
                    'type': 'integer',
                    'nullable': True
                },
                'IpcMode': {
                    'type': 'string',
                    'nullable': True
                },
                'PortBindings': {
                    'type': 'dict',
                    'nullable': True,
                    'schema': {}
                },
                'SecurityOpt': {
                    'nullable': True
                },
                'CapAdd': {
                    'nullable': True
                },
                'CpuCount': {
                    'type': 'integer',
                    'nullable': True
                },
                'MemorySwap': {
                    'type': 'integer',
                    'nullable': True
                },
                'OomKillDisable': {
                    'type': 'boolean',
                    'nullable': True
                },
                'LogConfig': {
                    'type': 'dict',
                    'nullable': True,
                    'schema': {
                        'Config': {
                            'type': 'dict',
                            'nullable': True,
                            'schema': {}
                        },
                        'Type': {
                            'type': 'string',
                            'nullable': True
                        }
                    }
                },
                'IOMaximumBandwidth': {
                    'type': 'integer',
                    'nullable': True
                }
            }
        },
        'Id': {
            'type': 'string',
            'nullable': True
        },
        'Ip': {
            'type': 'string',
            'nullable': True
        },
        'MountLabel': {
            'type': 'string',
            'nullable': True
        }
    }
}

Network = {
    'allow_unknown': True,
    'schema': {
        'Options': {
            'type': 'dict',
            'nullable': True,
            'schema': {
                'com.docker.network.bridge.name': {
                    'type': 'string',
                    'nullable': True
                },
                'com.docker.network.bridge.default_bridge': {
                    'type': 'string',
                    'nullable': True
                },
                'com.docker.network.bridge.enable_ip_masquerade': {
                    'type': 'string',
                    'nullable': True
                },
                'com.docker.network.driver.mtu': {
                    'type': 'string',
                    'nullable': True
                },
                'com.docker.network.bridge.host_binding_ipv4': {
                    'type': 'string',
                    'nullable': True
                },
                'com.docker.network.bridge.enable_icc': {
                    'type': 'string',
                    'nullable': True
                }
            }
        },
        'Name': {
            'type': 'string',
            'nullable': True
        },
        'Created': {
            'type': 'string',
            'nullable': True
        },
        'EnableIPv6': {
            'type': 'boolean',
            'nullable': True
        },
        'Labels': {
            'type': 'dict',
            'nullable': True,
            'schema': {}
        },
        'Driver': {
            'type': 'string',
            'nullable': True
        },
        'Attachable': {
            'type': 'boolean',
            'nullable': True
        },
        'Internal': {
            'type': 'boolean',
            'nullable': True
        },
        'IPAM': {
            'type': 'dict',
            'nullable': True,
            'schema': {
                'Config': {
                    'type': 'list',
                    'nullable': True,
                    'schema': {
                        'type': 'dict',
                        'nullable': True,
                        'schema': {
                            'Subnet': {
                                'type': 'string',
                                'nullable': True
                            },
                            'Gateway': {
                                'type': 'string',
                                'nullable': True
                            }
                        }
                    }
                },
                'Driver': {
                    'type': 'string',
                    'nullable': True
                },
                'Options': {
                    'nullable': True
                }
            }
        },
        'Scope': {
            'type': 'string',
            'nullable': True
        },
        'Id': {
            'type': 'string'
        },
        'Ip': {
            'type': 'string'
        },
        'Containers': {
            'type': 'dict',
            'nullable': True,
            'schema': {}
        }
    }
}

Service = {
    'allow_unknown': True,
    'schema': {
        'Endpoint': {
            'type': 'dict',
            'nullable': True,
            'schema': {
                'VirtualIPs': {
                    'type': 'list',
                    'nullable': True,
                    'schema': {
                        'type': 'dict',
                        'nullable': True,
                        'schema': {
                            'NetworkID': {
                                'type': 'string',
                                'nullable': True
                            },
                            'Addr': {
                                'type': 'string',
                                'nullable': True
                            }
                        }
                    }
                },
                'Spec': {
                    'type': 'dict',
                    'nullable': True,
                    'schema': {
                        'Mode': {
                            'type': 'string',
                            'nullable': True
                        },
                        'Ports': {
                            'type': 'list',
                            'nullable': True,
                            'schema': {
                                'type': 'dict',
                                'nullable': True,
                                'schema': {
                                    'TargetPort': {
                                        'type': 'integer',
                                        'nullable': True
                                    },
                                    'PublishedPort': {
                                        'type': 'integer',
                                        'nullable': True
                                    },
                                    'Protocol': {
                                        'type': 'string',
                                        'nullable': True
                                    },
                                    'PublishMode': {
                                        'type': 'string',
                                        'nullable': True
                                    }
                                }
                            }
                        }
                    }
                },
                'Ports': {
                    'type': 'list',
                    'nullable': True,
                    'schema': {
                        'type': 'dict',
                        'nullable': True,
                        'schema': {
                            'TargetPort': {
                                'type': 'integer',
                                'nullable': True
                            },
                            'PublishedPort': {
                                'type': 'integer',
                                'nullable': True
                            },
                            'Protocol': {
                                'type': 'string',
                                'nullable': True
                            },
                            'PublishMode': {
                                'type': 'string',
                                'nullable': True
                            }
                        }
                    }
                }
            }
        },
        'ID': {
            'type': 'string',
            'nullable': True
        },
        'Ip': {
            'type': 'string',
            'nullable': True
        },
        'Version': {
            'type': 'dict',
            'nullable': True,
            'schema': {
                'Index': {
                    'type': 'integer',
                    'nullable': True
                }
            }
        },
        'PreviousSpec': {
            'type': 'dict',
            'nullable': True,
            'schema': {
                'Name': {
                    'type': 'string',
                    'nullable': True
                },
                'EndpointSpec': {
                    'type': 'dict',
                    'nullable': True,
                    'schema': {
                        'Mode': {
                            'type': 'string',
                            'nullable': True
                        },
                        'Ports': {
                            'type': 'list',
                            'nullable': True,
                            'schema': {
                                'type': 'dict',
                                'nullable': True,
                                'schema': {
                                    'TargetPort': {
                                        'type': 'integer',
                                        'nullable': True
                                    },
                                    'PublishedPort': {
                                        'type': 'integer',
                                        'nullable': True
                                    },
                                    'Protocol': {
                                        'type': 'string',
                                        'nullable': True
                                    },
                                    'PublishMode': {
                                        'type': 'string',
                                        'nullable': True
                                    }
                                }
                            }
                        }
                    }
                },
                'UpdateConfig': {
                    'type': 'dict',
                    'nullable': True,
                    'schema': {
                        'MaxFailureRatio': {
                            'type': 'integer',
                            'nullable': True
                        },
                        'Parallelism': {
                            'type': 'integer',
                            'nullable': True
                        },
                        'FailureAction': {
                            'type': 'string',
                            'nullable': True
                        }
                    }
                },
                'Mode': {
                    'type': 'dict',
                    'nullable': True,
                    'schema': {
                        'Replicated': {
                            'type': 'dict',
                            'nullable': True,
                            'schema': {
                                'Replicas': {
                                    'type': 'integer',
                                    'nullable': True
                                }
                            }
                        }
                    }
                },
                'Networks': {
                    'type': 'list',
                    'nullable': True,
                    'schema': {
                        'type': 'dict',
                        'nullable': True,
                        'schema': {
                            'Target': {
                                'type': 'string',
                                'nullable': True
                            }
                        }
                    }
                },
                'TaskTemplate': {
                    'type': 'dict',
                    'nullable': True,
                    'schema': {
                        'Placement': {
                            'type': 'dict',
                            'nullable': True,
                            'schema': {}
                        },
                        'ContainerSpec': {
                            'type': 'dict',
                            'nullable': True,
                            'schema': {
                                'Image': {
                                    'type': 'string',
                                    'nullable': True
                                },
                                'DNSConfig': {
                                    'type': 'dict',
                                    'nullable': True,
                                    'schema': {}
                                },
                                'Env': {
                                    'type': 'list',
                                    'nullable': True,
                                    'schema': {
                                        'type': 'string',
                                        'nullable': True
                                    }
                                }
                            }
                        },
                        'Networks': {
                            'type': 'list',
                            'nullable': True,
                            'schema': {
                                'type': 'dict',
                                'nullable': True,
                                'schema': {
                                    'Target': {
                                        'type': 'string',
                                        'nullable': True
                                    }
                                }
                            }
                        },
                        'RestartPolicy': {
                            'type': 'dict',
                            'nullable': True,
                            'schema': {
                                'MaxAttempts': {
                                    'type': 'integer',
                                    'nullable': True
                                },
                                'Condition': {
                                    'type': 'string',
                                    'nullable': True
                                }
                            }
                        },
                        'ForceUpdate': {
                            'type': 'integer',
                            'nullable': True
                        },
                        'Resources': {
                            'type': 'dict',
                            'nullable': True,
                            'schema': {
                                'Reservations': {
                                    'type': 'dict',
                                    'nullable': True,
                                    'schema': {}
                                },
                                'Limits': {
                                    'type': 'dict',
                                    'nullable': True,
                                    'schema': {}
                                }
                            }
                        }
                    }
                }
            }
        },
        'UpdatedAt': {
            'type': 'string',
            'nullable': True
        },
        'UpdateStatus': {
            'type': 'dict',
            'nullable': True,
            'schema': {
                'StartedAt': {
                    'type': 'string',
                    'nullable': True
                },
                'CompletedAt': {
                    'type': 'string',
                    'nullable': True
                }
            }
        },
        'Spec': {
            'type': 'dict',
            'nullable': True,
            'schema': {
                'Name': {
                    'type': 'string',
                    'nullable': True
                },
                'EndpointSpec': {
                    'type': 'dict',
                    'nullable': True,
                    'schema': {
                        'Mode': {
                            'type': 'string',
                            'nullable': True
                        },
                        'Ports': {
                            'type': 'list',
                            'nullable': True,
                            'schema': {
                                'type': 'dict',
                                'nullable': True,
                                'schema': {
                                    'TargetPort': {
                                        'type': 'integer',
                                        'nullable': True
                                    },
                                    'PublishedPort': {
                                        'type': 'integer',
                                        'nullable': True
                                    },
                                    'Protocol': {
                                        'type': 'string',
                                        'nullable': True
                                    },
                                    'PublishMode': {
                                        'type': 'string',
                                        'nullable': True
                                    }
                                }
                            }
                        }
                    }
                },
                'UpdateConfig': {
                    'type': 'dict',
                    'nullable': True,
                    'schema': {
                        'MaxFailureRatio': {
                            'type': 'integer',
                            'nullable': True
                        },
                        'Parallelism': {
                            'type': 'integer',
                            'nullable': True
                        },
                        'FailureAction': {
                            'type': 'string',
                            'nullable': True
                        }
                    }
                },
                'Mode': {
                    'type': 'dict',
                    'nullable': True,
                    'schema': {
                        'Replicated': {
                            'type': 'dict',
                            'nullable': True,
                            'schema': {
                                'Replicas': {
                                    'type': 'integer',
                                    'nullable': True
                                }
                            }
                        }
                    }
                },
                'Networks': {
                    'type': 'list',
                    'nullable': True,
                    'schema': {
                        'type': 'dict',
                        'nullable': True,
                        'schema': {
                            'Target': {
                                'type': 'string',
                                'nullable': True
                            }
                        }
                    }
                },
                'TaskTemplate': {
                    'type': 'dict',
                    'nullable': True,
                    'schema': {
                        'Placement': {
                            'type': 'dict',
                            'nullable': True,
                            'schema': {}
                        },
                        'ContainerSpec': {
                            'type': 'dict',
                            'nullable': True,
                            'schema': {
                                'Image': {
                                    'type': 'string',
                                    'nullable': True
                                },
                                'DNSConfig': {
                                    'type': 'dict',
                                    'nullable': True,
                                    'schema': {}
                                },
                                'Env': {
                                    'type': 'list',
                                    'nullable': True,
                                    'schema': {
                                        'type': 'string',
                                        'nullable': True
                                    }
                                }
                            }
                        },
                        'Networks': {
                            'type': 'list',
                            'nullable': True,
                            'schema': {
                                'type': 'dict',
                                'nullable': True,
                                'schema': {
                                    'Target': {
                                        'type': 'string',
                                        'nullable': True
                                    }
                                }
                            }
                        },
                        'RestartPolicy': {
                            'type': 'dict',
                            'nullable': True,
                            'schema': {
                                'MaxAttempts': {
                                    'type': 'integer',
                                    'nullable': True
                                },
                                'Condition': {
                                    'type': 'string',
                                    'nullable': True
                                }
                            }
                        },
                        'ForceUpdate': {
                            'type': 'integer',
                            'nullable': True
                        },
                        'Resources': {
                            'type': 'dict',
                            'nullable': True,
                            'schema': {
                                'Reservations': {
                                    'type': 'dict',
                                    'nullable': True,
                                    'schema': {}
                                },
                                'Limits': {
                                    'type': 'dict',
                                    'nullable': True,
                                    'schema': {}
                                }
                            }
                        }
                    }
                }
            }
        },
        'CreatedAt': {
            'type': 'string',
            'nullable': True
        }
    }
}

Node = {
    'allow_unknown': True,
    'schema': {
        'Status': {
            'type': 'dict',
            'nullable': True,
            'schema': {
                'State': {
                    'type': 'string',
                    'nullable': True
                },
                'Addr': {
                    'type': 'string',
                    'nullable': True
                }
            }
        },
        'Description': {
            'type': 'dict',
            'nullable': True,
            'schema': {
                'Engine': {
                    'type': 'dict',
                    'nullable': True,
                    'schema': {
                        'Plugins': {
                            'type': 'list',
                            'nullable': True,
                            'schema': {
                                'type': 'dict',
                                'nullable': True,
                                'schema': {
                                    'Type': {
                                        'type': 'string',
                                        'nullable': True
                                    },
                                    'Name': {
                                        'type': 'string',
                                        'nullable': True
                                    }
                                }
                            }
                        },
                        'EngineVersion': {
                            'type': 'string',
                            'nullable': True
                        }
                    }
                },
                'Platform': {
                    'type': 'dict',
                    'nullable': True,
                    'schema': {
                        'OS': {
                            'type': 'string',
                            'nullable': True
                        },
                        'Architecture': {
                            'type': 'string',
                            'nullable': True
                        }
                    }
                },
                'Hostname': {
                    'type': 'string',
                    'nullable': True
                },
                'Resources': {
                    'type': 'dict',
                    'nullable': True,
                    'schema': {
                        'MemoryBytes': {
                            'type': 'integer',
                            'nullable': True
                        },
                        'NanoCPUs': {
                            'type': 'integer',
                            'nullable': True
                        }
                    }
                }
            }
        },
        'ID': {
            'type': 'string',
            'nullable': True
        },
        'Ip': {
            'type': 'string',
            'nullable': True
        },
        'Version': {
            'type': 'dict',
            'nullable': True,
            'schema': {
                'Index': {
                    'type': 'integer',
                    'nullable': True
                }
            }
        },
        'ManagerStatus': {
            'type': 'dict',
            'nullable': True,
            'schema': {
                'Reachability': {
                    'type': 'string',
                    'nullable': True
                },
                'Leader': {
                    'type': 'boolean',
                    'nullable': True
                },
                'Addr': {
                    'type': 'string',
                    'nullable': True
                }
            }
        },
        'UpdatedAt': {
            'type': 'string',
            'nullable': True
        },
        'Spec': {
            'type': 'dict',
            'nullable': True,
            'schema': {
                'Role': {
                    'type': 'string',
                    'nullable': True
                },
                'Availability': {
                    'type': 'string',
                    'nullable': True
                }
            }
        },
        'CreatedAt': {
            'type': 'string',
            'nullable': True
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
