script_path=$(dirname "$(readlink -f "$0")")

cat <<EOF | sudo tee /etc/systemd/system/tunneling.service >/dev/null
[Unit]
Description=tunneling Service
After=network.target

[Service]
Type=simple
ExecStart=${script_path}/run.sh
Restart=always

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl daemon-reload