def import_notes(lines):
    result = []
    for line in lines:
        parts = line.strip().split(' ')
        time_slot = []
        for i in range(len(parts))[::2]:
            time_slot.append({
                'note': parts[i],
                'duration': float(parts[i+1])
            })
        result.append(time_slot)
    return result


def export_notes(song):
    result = ''
    for time_slot in song:
        time_slot = list(map(lambda note: f"{note['note']} {note['duration']}", time_slot))
        result += ' '.join(time_slot) + '\n'
    return result
