import player, buildings, tables, units

start_status = input('Start a new game? y/n')
if start_status == 'y':
    ruler = player.Player()
    ruler.output_status()
    selected_item = ruler.get_action()
    if selected_item == 'worker':
        if ruler.workers:
            print('You have '+str(len(ruler.workers))+' workers.')
            print('Select which one?')
