mplayer px.audio.mp3 &> /dev/null &
while ! [[ -f stop ]]; do
    sleep 1
done
rm stop
kill $(ps -aux | grep px.audio.mp3 | head -n 1 | awk '{print $2}')
exit 
