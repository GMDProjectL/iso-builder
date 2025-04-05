clear

if [[ $(glxinfo | grep "OpenGL renderer") == *"llvmpipe"* ]]; then
  echo "LISTEN, YOU! DO YOU UNDERSTAND THAT YOU ARE RUNNING ON A SOFTWARE RENDERER? PLEASE DON'T DO THAT!";
  echo -e "\033[91mGPU NOT DETECTED!\033[0m"

  echo "..."
  echo "..."
  echo "...or if you really want to, you can go ahead.";
  read -p "Press enter to continue..."
fi

if [[ $(lspci -vnn | grep VGA | grep -i "VirtualBox") != "" ]]; then
  echo "LISTEN, YOU! DO YOU UNDERSTAND THAT YOU ARE RUNNING ON A VIRTUALBOX GPU? PLEASE DON'T DO THAT!";
  echo -e "\033[91mVIRTUALBOX DETECTED!\033[0m"

  echo "..."
  echo "..."
  echo "...or if you really want to, you can go ahead. This is the last warning.";
  read -p "Press enter to continue..."
fi


if [[ $(tty) = "/dev/tty1" ]]; then
	Hyprland
fi
