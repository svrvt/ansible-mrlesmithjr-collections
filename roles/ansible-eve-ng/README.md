# ansible-eve-ng

An Ansible role to install [Eve-NG Community](https://www.eve-ng.net/community/community-2).

## Requirements

Interfaces must use old ethx naming.

> NOTE: These changes are also made as part of the original provisioning of
> this role if this is not already done.

```bash
sudo vi /etc/default/grub
```

Ensure that `GRUB_CMDLINE_LINUX` line matches:

```bash
GRUB_CMDLINE_LINUX="net.ifnames=0 biosdevname=0"
```

Once the above has been changed:

```bash
grub-mkconfig -o /boot/grub/grub.cfg
```

## Role Variables

## Dependencies

## Example Playbook

## License

## Author Information
