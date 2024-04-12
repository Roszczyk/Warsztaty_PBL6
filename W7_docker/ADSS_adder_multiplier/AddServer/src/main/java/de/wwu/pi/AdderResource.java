package de.wwu.pi;

import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.QueryParam;
import javax.ws.rs.core.MediaType;

@Path("/")
public class AdderResource {

	@GET
	@Produces(MediaType.APPLICATION_JSON)
	public int addTwoNumbers(
			@QueryParam("first") int first,
			@QueryParam("second") int second) {
		return first + second;
	}

}
