ssh-keygen -q -t ed25519 -N '' -f ~/.ssh/id_ed25519 -C "rahulsanjay18@gmail.com" <<< y

curl -H "Authorization: token $1" --data '{"title": "$(hostname)", "key": $(cat ~/.ssh/id_ed25519.pub)}' https://api.github.com/user/keys

cd ~/Documents

git clone git@github.com:rahulsanjay18/master_server_docs.git

cd master_server_docs

git config --global user.email "rahulsanjay18@gmail.com"
git config --global user.name "Rahul Shah"
