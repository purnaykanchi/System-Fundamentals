def fcfs(seq,head):
    seek_seq=[]
    curr_track=head
    for track in seq:
        seek_seq.append(abs(curr_track-track))
        curr_track=track
    total_seek_time=sum(seek_seq)*6
    return total_seek_time
seq=[20,10,22,20,2,40,6,38]
head_pos=20
fcfs_seek_time=fcfs(seq,head_pos)
print(f"FCFS Total Seek Time:{fcfs_seek_time}ms")