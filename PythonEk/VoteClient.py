import grpc
import vote_pb2
import vote_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = vote_pb2_grpc.VoteServiceStub(channel)

    # Sende die Anfrage mit dem korrekt benannten Feld
    request = vote_pb2.VoteRequest(VoteId="1")

    try:
        # Hole die Antwort vom Server
        response = stub.getVoteData(request)
        print(f"Vote ID: {response.VoteId}")
        for candidate in response.candidates:
            print(f"Candidate Name: {candidate.candidateName}, Votes: {candidate.votes}")
    except grpc.RpcError as e:
        print(f"gRPC error: {e}")

    channel.close()

if __name__ == '__main__':
    run()
