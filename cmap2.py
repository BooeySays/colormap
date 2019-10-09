function __cmap2()
{
echo -e "\n\n[01mＥｘｔｒａ ｃｏｌｏｒｓ ：[m\n"
xxx=16
while [ $xxx -lt 231 ]; do
	while [ $xxx -lt 100 ]; do
		echo -en "[01m "$xxx"[m:[00;38;5;"$xxx"m▆▆▆▆▆▆[m  "
		((xxx +=1))
		echo -en "[01m "$xxx"[m:[00;38;5;"$xxx"m▆▆▆▆▆▆[m  "
		((xxx +=1))
		echo -en "[01m "$xxx"[m:[00;38;5;"$xxx"m▆▆▆▆▆▆[m  "
		((xxx +=1))
		echo -en "[01m "$xxx"[m:[00;38;5;"$xxx"m▆▆▆▆▆▆[m  "
		((xxx +=1))
		echo -en "[01m "$xxx"[m:[00;38;5;"$xxx"m▆▆▆▆▆▆[m  "
		((xxx +=1))
		echo -e "[01m "$xxx"[m:[00;38;5;"$xxx"m▆▆▆▆▆▆[m  "
		((xxx +=1))
	done
	echo -en "[01m"$xxx"[m:[00;38;5;"$xxx"m▆▆▆▆▆▆[m  "
	((xxx +=1))
	echo -en "[01m"$xxx"[m:[00;38;5;"$xxx"m▆▆▆▆▆▆[m  "
	((xxx +=1))
	echo -en "[01m"$xxx"[m:[00;38;5;"$xxx"m▆▆▆▆▆▆[m  "
	((xxx +=1))
	echo -en "[01m"$xxx"[m:[00;38;5;"$xxx"m▆▆▆▆▆▆[m  "
	((xxx +=1))
	echo -en "[01m"$xxx"[m:[00;38;5;"$xxx"m▆▆▆▆▆▆[m  "
	((xxx +=1))
	echo -e "[01m"$xxx"[m:[00;38;5;"$xxx"m▆▆▆▆▆▆[m  "
	((xxx +=1))
done
}
