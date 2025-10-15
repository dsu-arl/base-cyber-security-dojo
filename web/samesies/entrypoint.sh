#!/bin/sh
# add custom hosts if they aren't already present
grep -q "minnetonkatriplets.test" /etc/hosts || echo "127.0.0.1 minnetonkatriplets.test" >> /etc/hosts
grep -q "attacker.test" /etc/hosts || echo "127.0.0.1 attacker.test" >> /etc/hosts

# exec the container's main process (preserve signals)
exec "$@"