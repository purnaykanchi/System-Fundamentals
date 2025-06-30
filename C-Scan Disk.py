def c_scan(seq, head):
     seek_seq=[]
     curr_track=head
     left,right,dist=[],[],0
     for track in seq:
          if track<head:
               left.append(track)
          elif track>head:
               right.append(track)
     left,right=sorted(left,reverse=True),sorted(right)
     seek_seq.extend(right)
     seek_seq.extend(left)
     for track in seek_seq:
          dist+=abs(curr_track-track)
          curr_track=track
     total_seek_time=dist*6
     return total_seek_time
#INPUT
seq=[20,10,22,20,2,40,6,38]
head_pos=20
c_scan_seek_time=c_scan(seq,head_pos)
print(f"s-scan Total Seek Time:{c_scan_seek_time}ms")