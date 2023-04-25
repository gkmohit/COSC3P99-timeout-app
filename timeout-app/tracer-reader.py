import babeltrace

# Specify the path to the trace directory
trace_path = "/path/to/lttng/trace/directory"

# Create a trace collection
trace_collection = babeltrace.TraceCollection()

# Add trace directory to the collection
if trace_collection.add_trace(trace_path, "ctf") < 0:
    raise Exception("Error adding trace")

# Go through each event in the trace
for event in trace_collection.events:
    # Access event fields using event.field_name
    # For example, to access the timestamp and event name:
    timestamp = event.timestamp
    event_name = event.name

    # Access event context fields using event.context_field_name
    # For example, to access the CPU ID and PID:
    cpu_id = event["cpu_id"]
    pid = event["pid"]

    # Access event payload fields using event.payload_field_name
    # For example, to access an integer field called "value":
    value = event["value"]

    # Process event data as needed
    print(f"Timestamp: {timestamp}, Event: {event_name}, CPU ID: {cpu_id}, PID: {pid}, Value: {value}")

# Clean up the trace collection
trace_collection.clear()
