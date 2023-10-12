def tower_of_hanoi(n_disk, sou_disk, dest_disk, spar_disk):
    if n_disk == 1:
        print(f"Move disk 1 from {sou_disk} to {dest_disk}")
        return
    tower_of_hanoi(n_disk - 1, sou_disk, spar_disk, dest_disk)
    print(f"Move disk {n_disk} from {sou_disk} to {dest_disk}")
    tower_of_hanoi(n_disk - 1, spar_disk, dest_disk, sou_disk)

number_disk = int(input("Enter the number of disks : "))
tower_of_hanoi(number_disk, 'A', 'C', 'B')
